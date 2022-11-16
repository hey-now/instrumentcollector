from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class InstrumentCreate(CreateView):
    model = Instrument
    fields = '__all__'

class InstrumentUpdate(UpdateView):
    model = Instrument
    fields = ['type', 'brand', 'model', 'color', 'manf_date']

class InstrumentDelete(DeleteView):
    model = Instrument
    success_url = '/instruments'