
# Architecture Documentation

## Application Structure

```
myshop/
│
├── shop/          # Product catalog logic
├── cart/          # Session-based cart system
├── orders/        # Order & order item models
├── payment/       # Stripe integration
├── myshop/        # Project settings & Celery config
```

---

## Request Lifecycle

1. User browses products
2. Cart stored in session
3. Checkout creates Order instance
4. Stripe Checkout session created
5. Redirect to Stripe
6. On success → order marked pending confirmation
7. Celery task triggered for email processing

---

## Data Integrity Design

* OrderItem stores product price at purchase time.
* Cart is ephemeral and session-based.
* Order becomes immutable record of transaction.

---

## Asynchronous Task Flow

```
Django View
   ↓
Celery Task (delay())
   ↓
RabbitMQ Broker
   ↓
Worker Process
   ↓
Email Sent
```

Worker runs independently from web server process.

---

## Security Considerations

* Stripe hosted checkout avoids handling raw card data
* Secret keys stored in settings
* No sensitive data stored in session

---
