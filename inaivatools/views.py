from django.shortcuts import render, redirect

def index(request):
    return redirect('dashboard') if request.user.is_authenticated else render(request, 'index.html')

def dashboard(request):
    render(request, 'dashboard.html') if request.user.is_authenticatedrender else render(request, 'index.html')

def render_support_page(request):
    return render(request, 'otherPages/support.html')