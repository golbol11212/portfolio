from django.urls import path
from . import views

urlpatterns = [
    path('', views.midl_view, name='midl'),
    path('send_email/', views.send_email_view, name='send_email'),
]
