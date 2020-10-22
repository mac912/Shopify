#from django.contrib import admin
from django.urls import path, include

from .views import (
    SearchProductListView,
)

urlpatterns = [
    path('', SearchProductListView.as_view(), name='query'),
]
