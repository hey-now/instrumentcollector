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
def instruments_detail(request, instrument_id):
    instrument = Instrument.objects.get(id=instrument_id)
    return render(request, 'instruments/detail.html', { 'instrument': instrument })