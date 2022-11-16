from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page),
    path('search', views.search_product),
    path('product/<str:name>/<int:pk>', views.current_product),
    path('category/<int:pk>', views.get_current_category),
    path('add_product/<int:pk>', views.add_product_to_user_cart),
    path('cart', views.get_user_cart),
    path('delete-product/<int:pk>', views.delete_product_from_cart),
    path('send-to-tg', views.confirm_order)
]

