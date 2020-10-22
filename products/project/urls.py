"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from home.views import (home_page,
view, 
login_page, 
_logout,
register_page,
)
from product.views import (
ProductDetailSlugView,
#ProductListView,
#list_view,
#ProductDetailView,
#Detail_view,
#ProductFeaturedDetailView, 
#ProductFeaturedListView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include(("product.urls", "products"), namespace='products')),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('search/', include(("search.urls", "search"), namespace='search')),
    path('cart/', include(("cart.urls", "cart"), namespace='cart')),
    path('home/', home_page, name='home'),
    path('view/', view, name='view'),
    path('login/', login_page, name='login'), 
    path('', home_page, name='home'),
    path('logout/', _logout, name='logout'), 
    path('register/', register_page, name='register'), 
    

    #path('featured/<int:pk>', ProductFeaturedDetailView.as_view()),
    #path('featured/', ProductFeaturedListView.as_view()),
    #path('products-f/', list_view),
    #path('products/<int:pk>', ProductDetailView.as_view()),
    #path('products/<slug:slug>', ProductDetailSlugView.as_view()),
    #path('products-f/<int:pk>', Detail_view),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)