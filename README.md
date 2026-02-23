

# Django Online Shop 🛒

A full-stack e-commerce web application built with Django 6, featuring session-based cart management, asynchronous background processing with Celery + RabbitMQ, and Stripe Checkout integration.

This project demonstrates production-style backend architecture, payment integration, and task queue management.

---

## 🔍 Project Overview

This application simulates a real-world online store workflow:

Product browsing → Cart → Order creation → Stripe Checkout → Background task processing.

The focus of this project is clean architecture, separation of concerns, and scalable backend patterns.

---

## 🚀 Key Features

### 🧱 Product Catalog

* Category & Product models with slug-based URLs
* Optimized Django admin interface
* Media/image handling with Django media system
* SEO-friendly structure

---

### 🛒 Session-Based Shopping Cart

* Cart stored in session (avoids unnecessary DB writes)
* Custom context processor for global cart access
* Add / remove / update quantity
* Real-time total calculation

**Engineering decision:**
Session storage improves performance and reduces database load for anonymous users.

---

### 📦 Order Management

* Orders persisted in relational database
* OrderItem model maintains product-price snapshot
* Clean separation between cart and order logic

**Engineering decision:**
Price is copied into OrderItem to preserve historical pricing integrity.

---

### ⚙️ Asynchronous Processing (Celery + RabbitMQ)

* Celery configured as distributed task queue
* RabbitMQ used as message broker (Dockerized)
* Background task for order confirmation emails

**Why this matters:**
User does not wait for email sending or heavy processing.
Improves UX and system scalability.

---

### 💳 Stripe Payment Integration

* Stripe Checkout Session dynamically generated per order
* Secure use of Stripe secret & publishable keys
* Metadata used to associate Stripe session with internal Order ID
* Success & cancel views implemented

**Engineering focus:**
Payment logic is isolated from order creation.
Stripe handles PCI compliance through hosted checkout.

---

## 🏗️ Architecture Overview

```
User → Django Views → Cart (Session)
                     ↓
                Order Creation (DB)
                     ↓
             Stripe Checkout Session
                     ↓
         Celery Task (RabbitMQ Broker)
                     ↓
              Background Email Task
```

The system separates:

* Request handling
* Persistence layer
* Payment processing
* Background tasks

This mirrors production-grade web application architecture.

---

## 🛠️ Tech Stack

Backend: Django 6
Database: SQLite (dev)
Task Queue: Celery
Message Broker: RabbitMQ (Docker)
Payments: Stripe API (Checkout)
Containerization: Docker
Frontend: HTML5, CSS

---

## ⚙️ Local Setup

### Clone

```
git clone https://github.com/JustusJackline/myshop.git
cd myshop
```

### Virtual Environment

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Stripe Configuration

Add to `settings.py`:

```
STRIPE_SECRET_KEY=your_secret_key
STRIPE_PUBLISHABLE_KEY=your_publishable_key
API_VERSION=2023-10-16
```

---

### Start RabbitMQ (Docker)

```
sudo docker run -d --name rabbitmq \
  -p 5672:5672 \
  -p 15672:15672 \
  rabbitmq:3.13.1-management
```

---

### Run Celery Worker

```
celery -A myshop worker -l info
```

---

### Run Django

```
python manage.py migrate
python manage.py runserver
```

---

## 📈 What This Project Demonstrates

* RESTful backend architecture
* Task queue integration
* Payment gateway integration
* Clean separation of business logic
* Scalable background processing patterns

---

## 🔜 Next Enhancements

* Stripe webhooks for automatic order state updates
* PDF invoice generation
* PostgreSQL production configuration
* Deployment (Docker Compose + Nginx)
* CI/CD pipeline

