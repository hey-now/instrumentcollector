from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Instrument
from .forms import PlayedForm

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
    played_form = PlayedForm()
    return render(request, 'instruments/detail.html', {
         'instrument': instrument,
         'played_form': played_form
         })
def add_played(request, instrument_id):
    form = PlayedForm(request.POST)
    if form.is_valid():
        new_played = form.save(commit=False)
        new_played.instrument_id = instrument_id
        new_played.save()
    return redirect('detail', instrument_id=instrument_id)

class InstrumentCreate(CreateView):
    model = Instrument
    fields = '__all__'

class InstrumentUpdate(UpdateView):
    model = Instrument
    fields = ['type', 'brand', 'model', 'color', 'manf_date']

class InstrumentDelete(DeleteView):
    model = Instrument
    success_url = '/instruments'