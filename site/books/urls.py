from django.urls import path
from django.views.generic import TemplateView
from books.views import index, books, detail


app_name = 'books'

urlpatterns = [
    #path('', TemplateView.as_view(template_name='base.html'), name='index'),
    path('', index, name='index'),
    path('category/<slug:category_slug>/', books, name='category'),
    path('<slug:slug_name>/', detail, name='detail')
]
