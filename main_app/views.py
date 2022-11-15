from django.shortcuts import render
from .models import Instrument

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def instruments_index(request):
    instruments = Instrument.objects.all()
    return render(request, 'instruments/index.html', { 'instruments': instruments })