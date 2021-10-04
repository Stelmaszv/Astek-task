from apps.carts.views import CartList
from django.urls import path
app_name = 'carts'

urlpatterns = [
    path('carts',    CartList.as_view(), name='carts_list')
]