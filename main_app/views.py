from django.shortcuts import render

instruments = [
    {'imgURL': 'https://imgur.com/hL0AvIC.jpeg', 'nickname': 'Ole Faithful', 'type': 'Guitar', 'brand': 'Schecter', 'model': 'Diamond Series C-1', 'color': 'Flame', 'manufactured_date': '2002'},
    {'imgURL': 'https://imgur.com/ksNv6KU.jpeg', 'nickname': 'Showstopper', 'type': 'Guitar', 'brand': 'Martin', 'model': 'Road Series SC-10E', 'color': 'Satin Spruce', 'manufactured_date': '2022'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def instruments_index(request):
    return render(request, 'instruments/index.html', { 'instruments': instruments })