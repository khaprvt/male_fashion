from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, DetailView
from .models import ProductModel, CategoryModel, BrandModel, TagModel, ColorModel, SizeModel, WishlistModel
from django.db.models import Max, Min

# Create your views here.

class ShoppingCartView(ListView):
    template_name = 'main/shopping-cart.html'

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        qs = ProductModel.get_cart_objects(cart)
        return qs


def cart_view(request, id):
    cart = request.session.get('cart', [])
    if not cart:
        request.session['cart'] = []
        cart = request.session.get('cart', [])

    if id in cart:
        cart.remove(id)
    else:
        cart.append(id)

    request.session['cart'] = cart
    path = request.GET.get('next', '/')
    return redirect(path)



class WishlistListView(ListView):
    template_name = 'main/wishlist.html'
    paginate_by = 12

    def get_queryset(self):
        qs = ProductModel.objects.filter(wishlistmodel__user=self.request.user)
        sort = self.request.GET.get('sort')
        if sort:
            qs = qs.order_by(sort)
        if sort == 'sale':
            qs = qs.filter(sale=True)
        return qs


def wishlist_view(request, id):
    product = ProductModel.objects.get(id=id)
    WishlistModel.create_or_delete(request.user, product)
    path = request.GET.get('next', '')
    return redirect(path)




class ProductDetailView(DetailView):
    template_name = 'main/shop-details.html'
    model = ProductModel

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['products'] = ProductModel.objects.all().exclude(id=self.object.id)[:4]
        return data


class ProductListView(ListView):
    template_name = 'main/shop.html'
    model = ProductModel
    paginate_by = 9
    
    
    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)

        cat = self.request.GET.get('cat')
        if cat:
            qs = qs.filter(category=cat)

        brand = self.request.GET.get('brand')
        if brand:
            qs = qs.filter(brand=brand)


        price = self.request.GET.get('price')
        if price:
            price = price.split(';')
            qs = qs.filter(real_price__gte=price[0], real_price__lte=price[1])


        size = self.request.GET.get('size')
        if size:
            qs = qs.filter(size=size)


        color = self.request.GET.get('color')
        if color:
            qs = qs.filter(color=color)


        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tag=tag)


        sort = self.request.GET.get('sort')
        if sort:
            qs = qs.order_by(sort)
        if sort == 'sale':
            qs = qs.filter(sale=True)

        return qs
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['sizes'] = SizeModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        context['tags'] = TagModel.objects.all()
        context['min'], context['max'] = ProductModel.objects.all().aggregate(Min('real_price'), Max('real_price')).values()
        return context
