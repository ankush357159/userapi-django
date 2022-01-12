from django.urls import path
from rest_framework import views
from api.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view())
]