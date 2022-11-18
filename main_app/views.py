from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Instrument, Accessory
from .forms import PlayedForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def instruments_index(request):
    instruments = Instrument.objects.all()
    return render(request, 'instruments/index.html', { 'instruments': instruments })

def instruments_guitars(request):
    instruments = Instrument.objects.filter(type='Guitar')
    return render(request, 'instruments/guitars.html', { 'instruments': instruments })

def instruments_keyboards(request):
    instruments = Instrument.objects.filter(type='Keyboard')
    return render(request, 'instruments/guitars.html', { 'instruments': instruments })

def instruments_detail(request, instrument_id):
    instrument = Instrument.objects.get(id=instrument_id)
    id_list = instrument.accessories.all().values_list('id')
    accessories_instrument_doesnt_have = Accessory.objects.exclude(id__in=id_list)
    played_form = PlayedForm()
    return render(request, 'instruments/detail.html', {
         'instrument': instrument,
         'played_form': played_form,
         'accessories': accessories_instrument_doesnt_have
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
    fields = ['img_Url', 'nickname', 'type', 'brand', 'model', 'color', 'manf_date']

class InstrumentUpdate(UpdateView):
    model = Instrument
    fields = ['img_Url', 'type', 'brand', 'model', 'color', 'manf_date']

class InstrumentDelete(DeleteView):
    model = Instrument
    success_url = '/instruments'

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'type']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories'

def assoc_accessory(requst, instrument_id, accessory_id):
    Instrument.objects.get(id=instrument_id).accessories.add(accessory_id)
    return redirect('detail', instrument_id=instrument_id)

def unassoc_accessory(requst, instrument_id, accessory_id):
    Instrument.objects.get(id=instrument_id).accessories.remove(accessory_id)
    return redirect('detail', instrument_id=instrument_id)