from django.urls import path
# import mainapp.views as mainapp
from mainapp.views import products, product

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
    path('product/<int:pk>/', product, name='detail'),
]
