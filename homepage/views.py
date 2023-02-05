from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def foodDeals(request):
    return render(request, 'food-deals.html', {})

def search(request):
    return render(request, 'search.html', {})

def about(request):
    return render(request, 'about.html', {})

def FAQ(request):
    return render(request, 'FAQ.html', {})


