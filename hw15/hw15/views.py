from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def products(request):
    products_list = [
        {
            "image_url": "https://via.placeholder.com/150",
            "name": "Product1",
            "description": "rgarrgw",
            "price": 100,
        },
        {
            "image_url": "https://via.placeholder.com/150",
            "name": "Product2",
            "description": "Оwgagw",
            "price": 200,
        },
    ]

    return render(request, "products.html", {
        "products": products_list
    })


def profile(request):
    return render(request, "profile.html")


def contact(request):
    return render(request, "contact.html")
