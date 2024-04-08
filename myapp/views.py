from .models import Product, Customer, Employee,Bill,ProductItem,BillItem
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import AddProductItemForm,AddProductForm, ProductForm, AddCustomerForm,AddProductToBillForm,LoginForm,BillForm
import json
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from rest_framework.decorators import api_view

@api_view(['GET'])
def generate_bill_pdf(request, bill_id):
    # Fetch the bill object from the database using the bill_id
    bill = Bill.objects.get(pk=bill_id)

    # Create a PDF buffer
    buffer = BytesIO()

    # Create a canvas object
    pdf = canvas.Canvas(buffer)

    # Draw the bill details on the PDF
    pdf.drawString(100, 800, f'Bill ID: {bill.id}')
    pdf.drawString(100, 780, f'Customer: {bill.customer}')
    pdf.drawString(100, 760, f'Total Amount: {bill.total_amount}')

    # Draw bill items
    y = 740
    for item in bill.billitem_set.all():
        pdf.drawString(120, y, f'Product: {item.product}')
        pdf.drawString(120, y - 20, f'Quantity: {item.quantity}')
        pdf.drawString(120, y - 40, f'Amount: {item.product.price * item.quantity}')
        y -= 60

    # Save the PDF
    pdf.save()

    # Get the PDF content from the buffer
    pdf_data = buffer.getvalue()
    buffer.close()

    # Create an HTTP response with PDF content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="bill_{bill.id}.pdf"'
    response.write(pdf_data)
    return response

@api_view(['GET','POST'])
def add_bill(request):
    if request.method == 'POST':
        bill_form = BillForm(request.POST)
        if bill_form.is_valid():
            # Save the bill instance
            bill = bill_form.save(commit=False)
            bill.employee_generated = Employee.objects.get(pk=request.session['employee_id'])
            bill.total_amount = 0  # Initialize total amount
            
            # Save the bill and retrieve its ID
            bill.save()
            
            print(request.POST.items())
            
            # Process bill items
            for key, value in request.POST.items():
                if key.startswith('product_'):
                    product_id = int(value)
                    quantity = int(request.POST.get(f'quantity_{key.split("_")[1]}'))
                    product = Product.objects.get(pk=product_id)
                    total_price = product.price * quantity
                    
                    # Create bill item
                    BillItem.objects.create(
                        bill=bill,
                        product=product,
                        quantity=quantity
                    )
                    
                    # Update total amount
                    bill.total_amount += total_price
            
            # Save the updated bill with total amount
            bill.save()
            
            pdf=generate_bill_pdf(request, bill.id)

            return pdf
    else:
        bill_form = BillForm()

    products = Product.objects.all()
    return render(request, 'add_bill.html', {'bill_form': bill_form, 'products': products})

@api_view(['GET',"POST"])
def add_customer(request):
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to the customer list page after adding the customer
    else:
        form = AddCustomerForm()
    
    return render(request, 'add_customer.html', {'form': form})

@api_view(['GET',"POST"])
def delete_customer(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return HttpResponse('Customer not found')
    
    customer.delete()
    return redirect('customer_list')

@api_view(['GET',"POST"])
def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list') 
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'update_product.html', {'form': form})

@api_view(['GET',"POST"])
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse('Product not found')
    
    product.delete()
    return redirect('product_list')

@api_view(['GET'])
def home(request):
    return render(request, 'home.html')

@api_view(['GET',"POST"])
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list page after adding the product
    else:
        form = AddProductForm()
    
    return render(request, 'add_product.html', {'form': form})

@api_view(['GET',"POST"])
def main_page(request):
    return render(request, 'main_page.html')

@api_view(['GET','POST'])
def index(request):
    username = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"Username: {username}, Password: {password}")
            try:
                employee = Employee.objects.get(username=username)
                if employee.check_password(password):
                    print("Password Check Successful!")
                    request.session['employee'] = employee.username
                    username = request.session['employee']
                    print(f"request.session['employee']: {request.session['employee']}")
                    request.session['employee_id'] = employee.id
                    print(request.session['employee_id'])
                    return redirect('home')
                else:
                    print("Invalid Password!")
                    form.add_error('password', 'Invalid password')
            except Employee.DoesNotExist:
                print("No user with that username")
                form.add_error('username', 'No employee with this username')
    else:
        form = LoginForm()
    print(f"Username final before returning: {username}")
    return render(request, 'index.html', {'form': form, 'username':username})

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@api_view(['GET'])
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})
