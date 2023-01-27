from django.urls import path
from . import views
from .views import ControlViews
from .views import CompaniesViews

urlpatterns = [
    path("", views.Upload_files),
    path("list", ControlViews.as_view()),
    path("companies", ControlViews.as_view()),
    path("companies/<nome_loja>", CompaniesViews.as_view()),
]
