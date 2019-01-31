#Location of non app single pages
from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:

        return render(request,'index.html')

def dashboard(request):
    return render(
    request,
    'dashboard.html'
)

def render_support_page(request):
    return render(
    request,
    'otherPages/support.html'
)