
Django Online Shop 🛒
An e-commerce web application built with Django 5, following Django 5 By Example (Antonio Melé).
The project demonstrates how to build a product catalog, a session-based shopping cart, order processing, and background task handling using Celery and RabbitMQ.
This repository reflects progress up to the asynchronous task processing (Celery + RabbitMQ) stage.
✨ Features Implemented So Far
Product Catalog
    • Category & Product Models
Products are organized into categories with slug-based, SEO-friendly URLs.
    • Admin Customization
The Django admin interface is customized to make managing products and categories easier and more intuitive.
    • Media & Images
Product images are handled using Django’s built-in media system.
Shopping Cart
    • Session-Based Cart
The shopping cart is stored in the user’s session, avoiding unnecessary database writes for every cart update.
    • Global Cart Access
A custom context processor ensures the cart (items, quantities, totals) is available across all templates.
    • Cart Operations
Users can add products, update quantities, remove items, and view real-time totals.
Orders & Background Processing
    • Order Management
Customers can place orders, and order details (including items and quantities) are persisted in the database.
    • Celery + RabbitMQ Integration
Background task processing is implemented using Celery with RabbitMQ as the message broker.
    • Asynchronous Tasks
Time-consuming operations (such as order confirmation emails) are processed asynchronously to keep the user experience fast and responsive.
🛠️ Tech Stack
    • Backend: Django 6
    • Database: SQLite (development) / PostgreSQL (production-ready)
    • Task Queue: Celery
    • Message Broker: RabbitMQ (Dockerized)
    • Frontend: HTML5, CSS
    • Containerization: Docker (for RabbitMQ)
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/JustusJackline/myshop.git
cd myshop
2. Set Up Virtual Environment
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
pip install -r requirements.txt
3. Start RabbitMQ (Docker)
RabbitMQ is required for Celery to work.
docker run -it --rm \
  --name rabbitmq \
  -p 5672:5672 \
  -p 15672:15672 \
  rabbitmq:3.13.1-management
RabbitMQ Management UI:
http://localhost:15672
(Default login: guest / guest)
4. Run Celery Worker
In a separate terminal (with the virtual environment activated):
celery -A myshop worker -l info
5.Run Django Development Server
python manage.py migrate
python manage.py runserver
Access the app at:
http://127.0.0.1:8000/
🚧 Next Steps
The next phase of the project focuses on payments and order lifecycle management, including:
    • Integrating Stripe for secure online payments
    • Handling Stripe webhooks to update order statuses automatically
    • Generating PDF invoices for completed orders
    • Improving order tracking and confirmation workflows
📚 Reference
This project is based on:
Antonio Melé — Django 5 By Example
