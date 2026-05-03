from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Product, Cart, UserProfile
from .forms import RegisterForm, LoginForm, ProfileForm


# 🌐 Landing Page
def landing(request):
    return render(request, 'landing.html')


# 🏠 Shop (Home Page)
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


# 📝 Register
def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        return redirect('login')

    return render(request, 'register.html', {'form': form})


# 🔐 Login
def user_login(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html', {'form': form})


# 🚪 Logout
def user_logout(request):
    logout(request)
    return redirect('landing')


# 👤 Profile
@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    form = ProfileForm(request.POST or None, instance=user_profile)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'profile.html', {'form': form})

# 🛒 Add to Cart
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('home')


# 🛍️ View Cart
@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


# ➕ Increase Quantity
@login_required
def increase_quantity(request, item_id):
    item = get_object_or_404(Cart, id=item_id)
    item.quantity += 1
    item.save()
    return redirect('cart')


# ➖ Decrease Quantity
@login_required
def decrease_quantity(request, item_id):
    item = get_object_or_404(Cart, id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()

    return redirect('cart')


# ❌ Remove Item
@login_required
def remove_item(request, item_id):
    item = get_object_or_404(Cart, id=item_id)
    item.delete()
    return redirect('cart')