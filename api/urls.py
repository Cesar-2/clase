from django.urls import path
from .views import UserApi,CarApi
urlpatterns = [
    path('users', UserApi.as_view()),
    path('cars',CarApi.as_view()),
]
