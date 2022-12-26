from django.urls import path

from .views import ListCreateSteps

urlpatterns = [
    path("", ListCreateSteps.as_view(), name="create_steps"),
]