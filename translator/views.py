from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#domain.com/
def index(request):
    return render(request, 'index.html')

def app(request):
    return render(request, 'app.html')