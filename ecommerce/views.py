from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})


def blog(request):
    return render(request, "blog.html", {})


def contact(request):
    return render(request, "contact.html", {})


def details(request):
    return render(request, "shop-details.html", {})


def cart(request):
    return render(request, "shoping-cart.html", {})


def checkout(request):
    return render(request, "checkout.html", {})


def blog_details(request):
    return render(request, "blog-details.html", {})
