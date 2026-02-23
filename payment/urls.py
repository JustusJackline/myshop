from django.urls import path

from .import views,webhook

app_name='payment'
urlpatterns=[
 path('process/',views.payment_process,name='process'),
 path('completed/',views.payment_completed,name='completed'),
 path('cancelled/',views.payment_cancelled,name='cancelled'),  
 path('webhook/',webhook.stripe_webhook,name='webhook'),
]