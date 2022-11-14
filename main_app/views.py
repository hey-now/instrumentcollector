from django.shortcuts import render

instruments = [
    {'type': 'Guitar', 'brand': 'Schecter', 'model': 'Diamond Series C-1', 'color': 'Sunburst', 'manufacture_date': '2002'},
    {'type': 'Guitar', 'brand': 'Martin', 'model': 'Road Series SC-10E', 'color': 'Satin Spruce', 'manufacture_date': '2022'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def instruments_index(request):
    return render(request, 'instruments/index.html', { 'instruments': instruments })