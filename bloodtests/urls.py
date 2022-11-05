from django.urls import path
from .views import TestDetails


urlpatterns = (
    path('test/', TestDetails.as_view()),
    path('test/<str:code>', TestDetails.as_view()),
)
