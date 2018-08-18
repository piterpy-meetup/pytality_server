from django.urls import path
from . import views

urlpatterns = [
    path('snippets/next/', views.get_next_snippet)
]