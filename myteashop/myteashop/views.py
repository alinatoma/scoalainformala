from django.shortcuts import render

def homepage_view(request):
    return render(request, 'homepage.html', {'title': 'Tea Party Shop'})

def contact_view(request):
    return render(request, 'contact.html', {'title': 'Tea Party Shop'})
