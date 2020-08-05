from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
from .views import FileUploadView

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('upload/', FileUploadView.as_view()),
]