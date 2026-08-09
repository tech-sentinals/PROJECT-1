from django.urls import path
from .views import check_symptoms, history

urlpatterns = [
    path("check/", check_symptoms, name="check_symptoms"),
    path("history/", history, name="history"),
]
