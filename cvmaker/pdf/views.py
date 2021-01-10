from django.shortcuts import render
from .models import Profile

# Create your views here.
def home(req):
    return render(req, "pdf/index.html")

