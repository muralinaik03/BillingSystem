## SPACE-Y BACKEND ASSIGNMENT

This repository contains the backend implementation for an on-counter billing system designed for a small-scale shopping mall. The project is built using Django and Django Rest Framework, utilizing Generic Views with a PostgreSQL database.

### Features Implemented

- **Authentication**
  - Employees can authenticate to access the system.

- **Product Management**
  - **Add, Update, Delete**: Products can be added to, updated in, or deleted from the system.

- **Customer Management**
  - **Add, Update, Delete**: Customers can be added to, updated in, or deleted from the system.

- **Billing**
  - Customers can be billed using the on-counter billing system with cash payment.

### URLs

- **Home**: `/home/` - Main landing page of the application.
- **Products**: `/products/` - Endpoint to manage products.
- **Customers**: `/customers/` - Endpoint to manage customers.
- **Main Page**: `/main/` - Main page of the application.
- **Add Bill**: `/add_bill/` - Endpoint to create a bill for a customer.
- **Add Product**: `/add_product/` - Endpoint to add a new product.
- **Product List**: `/product_list/` - Endpoint to list all products.
- **Customer List**: `/customer_list/` - Endpoint to list all customers.
- **Delete Product**: `/delete_product/<int:product_id>/` - Endpoint to delete a specific product.
- **Update Product**: `/update_product/<int:product_id>/` - Endpoint to update a specific product.
- **Delete Customer**: `/delete_customer/<int:customer_id>/` - Endpoint to delete a specific customer.
- **Add Customer**: `/add_customer/` - Endpoint to add a new customer.

### Deployment

The application has been deployed on Render and can be accessed at [Render App URL](https://billingsystemgu.onrender.com).

### API Documentation (Swagger UI)

The API documentation is available via Swagger UI at `/swagger`. Note that this currently returns HTML documentation and is not integrated directly with the REST API.

### Installation
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies using `pip install -r requirements.txt`.
4. Run the server using `python manage.py runserver`.

### Admin dashboard credentials (/admin)
- **Username**: admin
- **Password**: admin

### Employee login credentials
- **Username**: Emp1
- **Password**: 123
