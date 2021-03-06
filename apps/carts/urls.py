from apps.carts.views import CartList,CartListUser,CartListUserOrderBy,CartListUserSearch
from django.urls import path
app_name = 'carts'

urlpatterns = [
    path('carts',                    CartList.as_view(), name='carts_list'),
    path('',                         CartListUser.as_view(), name='carts_list_user'),
    path('<str:orderby>',            CartListUserOrderBy.as_view(), name='carts_list_user'),
    path('searchbyname/<str:name>',  CartListUserSearch.as_view(), name='carts_list_user'),
]