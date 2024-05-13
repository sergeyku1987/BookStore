from django.db import models
from django.core.validators import MaxValueValidator



class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=64, unique=True, verbose_name='url')

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True, verbose_name='url')
    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
        related_name='books'
    )
    description = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.PositiveIntegerField(blank=True, default=0, validators=[MaxValueValidator(99)])
    quantity = models.PositiveSmallIntegerField()
    category = models.ForeignKey(
        to=Category,
        on_delete=models.PROTECT,
        related_name='books',
    )

    class Meta:
        db_table = 'book'
        verbose_name = 'book'
        verbose_name_plural = 'books'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)

    class Meta:
        db_table = 'author'
        verbose_name = 'author'
        verbose_name_plural = 'authors'
    
    def __str__(self):
        return f'{self.first_name} {self.second_name}'