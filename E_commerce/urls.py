from django.urls import path
from . import views

urlpatterns = [
path('checkout/', views.checkout, name='checkout'),
    path('', views.landing, name='landing'),
    path('shop/', views.home, name='home'),
path('create-admin/', views.create_admin),

    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),

    path('profile/', views.profile, name='profile'),

    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),

    path('increase/<int:item_id>/', views.increase_quantity, name='increase'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decrease'),
    path('remove/<int:item_id>/', views.remove_item, name='remove'),
]