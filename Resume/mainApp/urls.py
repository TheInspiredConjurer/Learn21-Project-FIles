# URL creation for app, NOT FOR PROJECT.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('portfolio-details', views.portfoliodetails, name="portfolio-details"),
    path('success', views.success, name="form-submission-success"),
]