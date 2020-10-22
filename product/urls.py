#from django.contrib import admin
from django.urls import path
#from django.urls import url
#from django.conf import settings
#from django.conf.urls.static import static
from product.views import (
ProductDetailSlugView,
ProductListView,
#list_view,
#ProductDetailView,
#Detail_view,
#ProductFeaturedDetailView, 
#ProductFeaturedListView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
    #path('products-f/<int:pk>', Detail_view),
]
