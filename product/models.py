from django.db import models, Category
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 20, unique=True)
    slug = models.SlugField(max_length= 20, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.TextField()
    catetory = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='product/images/', blank=False)
    desc = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()

