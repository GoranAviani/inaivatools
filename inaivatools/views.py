#Location of non app single pages
from django.shortcuts import render


def render_support_page(request):
    return render(
    request,
    'otherPages/support.html'
)