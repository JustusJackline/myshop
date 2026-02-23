

# Django Online Shop 🛒

A full-stack e-commerce web application built with **Django 6**, featuring:

* Session-based cart management
* Asynchronous background processing with **Celery + RabbitMQ**
* **Stripe Checkout** integration

This project demonstrates production-style backend architecture, secure payment handling, and scalable task queue management.

---

## 🔍 Project Overview

This application simulates a real-world online store workflow:

**Product browsing → Cart → Order creation → Stripe Checkout → Background task processing**

Focus:

* Clean architecture
* Separation of concerns
* Scalable backend patterns
* Maintainable code for production-ready deployment

---

## 🚀 Key Features

### 🧱 Product Catalog

* Category & Product models with slug-based, SEO-friendly URLs
* Optimized Django admin interface for easier product management
* Media/image handling via Django’s media system

**Engineering decision:**
SEO-friendly URLs and a clean admin interface improve usability for both users and store managers.

---

### 🛒 Session-Based Shopping Cart

* Cart stored in user session to reduce database writes
* Custom context processor for global cart access in templates
* Add, remove, or update item quantities
* Real-time total calculation

**Engineering decision:**
Session storage improves performance and reduces DB load, especially for anonymous users.

---

### 📦 Order Management

* Orders persisted in relational database
* **OrderItem** model stores product-price snapshots for historical accuracy
* Clean separation between cart and order logic

**Engineering decision:**
Copying product price into **OrderItem** preserves order integrity even if product prices change later.

---

### ⚙️ Asynchronous Processing (Celery + RabbitMQ)

* Celery configured as distributed task queue
* RabbitMQ used as message broker (Dockerized)
* Background task for sending order confirmation emails

**Why this matters:**
Users don’t wait for heavy tasks like email sending, improving UX and system scalability.

---

💳 Stripe Payment Integration

Stripe Checkout Sessions dynamically created per order

Stripe secret and publishable keys securely stored in .env

Metadata links Stripe session to internal Order ID

Success & cancel views implemented

Engineering focus:
Payment logic is isolated from order creation. Stripe’s hosted checkout ensures PCI compliance and secure payment handling.
---

## 🏗️ Architecture Overview

```
User → Django Views → Cart (Session)
                     ↓
                Order Creation (Database)
                     ↓
             Stripe Checkout Session
                     ↓
         Celery Task (RabbitMQ Broker)
                     ↓
              Background Email Task
```

**System design highlights:**

* Clear separation of request handling, persistence, payment, and background tasks
* Mirrors production-grade web application architecture
* Supports asynchronous, non-blocking operations

---

## 🛠️ Tech Stack

* **Backend:** Django 6
* **Database:** SQLite (development), PostgreSQL (production-ready)
* **Task Queue:** Celery
* **Message Broker:** RabbitMQ (Dockerized)
* **Payments:** Stripe Checkout
* **Frontend:** HTML5, CSS
* **Containerization:** Docker (RabbitMQ)

---

## ⚙️ Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/JustusJackline/myshop.git
cd myshop
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3. Stripe Configuration

Create a `.env` file with your test keys:

```
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
```

> Do **not** commit `.env` to GitHub.

Update `settings.py`:

```python
from decouple import config

STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = config('STRIPE_PUBLISHABLE_KEY')
STRIPE_WEBHOOK_SECRET = config('STRIPE_WEBHOOK_SECRET')
```

---

### 4. Start RabbitMQ (Docker)

```bash
docker run -d --name rabbitmq \
  -p 5672:5672 \
  -p 15672:15672 \
  rabbitmq:3.13.1-management
```

Access RabbitMQ Management UI: [http://localhost:15672](http://localhost:15672)
(Default login: guest / guest)

---

### 5. Run Celery Worker

```bash
celery -A myshop worker -l info
```

---

### 6. Run Django Server

```bash
python manage.py migrate
python manage.py runserver 8080
```

> Use port `8080` to match your Stripe listener forward URL:
> `stripe listen --forward-to localhost:8080/payment/webhook/`

---

## 📈 What This Project Demonstrates

* Production-style RESTful backend architecture
* Task queue integration with Celery + RabbitMQ
* Stripe payment gateway integration
* Separation of business logic from payment and cart handling
* Scalable background processing patterns

---

## 🔜 Next Enhancements

* Generate PDF invoices for orders
* Deploy with **PostgreSQL**, Docker Compose, and Nginx
* CI/CD pipeline for automated testing and deployment
