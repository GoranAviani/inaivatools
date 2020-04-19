#Location of non app single pages
from django.shortcuts import render, redirect


def index(request):
    return redirect('dashboard') if request.user.is_authenticated else render(request, 'index.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return render (request,'index.html')

def render_support_page(request):
    return render(
    request,
    'otherPages/support.html'
)