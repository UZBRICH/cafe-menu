from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models

from .models import Product, Category, Feedback


# -------------------- MAIN PAGE (HOME + FEEDBACK) --------------------
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        rating = request.POST.get('rating')

        print("POST RECEIVED")
        print("DATA:", full_name, phone, message, rating)

        if full_name and message:
            Feedback.objects.create(
                full_name=full_name,
                phone=phone,
                message=message,
                rating=int(rating or 1)
            )

            messages.success(request, "Thanks! Your feedback was saved ❤️")
            return redirect('home')  # prevents resubmitting form

        else:
            messages.error(request, "Please fill all required fields!")

    feedbacks = Feedback.objects.all().order_by('-id')
    avg_rating = Feedback.objects.aggregate(models.Avg('rating'))['rating__avg']

    return render(request, 'index.html', {
        'products': products,
        'categories': categories,
        'feedbacks': feedbacks,
        'avg_rating': avg_rating
    })


# -------------------- MENU PAGE --------------------
def menu(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    avg_rating = Feedback.objects.aggregate(models.Avg('rating'))['rating__avg']

    return render(request, "menu.html", {
        "feedbacks": feedbacks,
        "avg_rating": avg_rating
    })