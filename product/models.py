import os
import random
from django.db import models
from django.db.models.signals import pre_save, post_save
from project.utils import unique_slug_generator
from django.urls import reverse

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
  
class ProductManager(models.Manager):
    def featured(self):
        return self.get_queryset().filter(featured = True)

    def get_by_id(self, id):
        qs =  self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

def upload_image_path(instance, filename):
    #print(filename)
    new_filename = random.randint(1, 45165615151)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename = new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

    #print(instance)
# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=40)
    image       = models.ImageField(upload_to='products/', null=True, blank=True)
    featured    = models.BooleanField(default=False)

    objects = ProductManager()

    def get_absolute_url(self):
        #return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:detail", kwargs={"slug":self.slug})


    def __str__(self):
        return self.title

    def __unicode__(self):
        print("hello")
        return self.title

    @property
    def name(self):
        return self.title

def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciever, sender=Product)