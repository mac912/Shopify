from django.db.models import Q
from django.shortcuts import render
from product.models import Product
from django.views.generic import ListView
# Create your views here.
class SearchProductListView(ListView):
    template_name = "view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', '')   #query = method_dict[q]    
        print(query)
        if query is not None:
            lookups = Q(title__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query) | Q(tag__title__icontains=query)
            return Product.objects.filter(lookups).distinct()    
        return Product.objects.featured()
