from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.register),
    path('login/', views.get_users),
    path('refresh/', TokenRefreshView.as_view()),
    # path('users/', views.get_users),
]