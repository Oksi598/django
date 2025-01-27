from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/category_detail.html', {'category': category, 'products': products})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'category']
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'category']
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'shop/category_form.html'
    success_url = reverse_lazy('product_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'shop/category_form.html'
    success_url = reverse_lazy('product_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'shop/category_confirm_delete.html'
    success_url = reverse_lazy('product_list')
