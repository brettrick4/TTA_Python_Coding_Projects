from django.shortcuts import render, redirect, get_object_or_404
from .models import LegoSet                     # import class of LegoSet to use object definition
from .models import MiniFig
from .forms import LegoSetForm                  # import Lego form to save to create and save new entries
from .forms import MiniFigForm
from .WeatherApi import *

# Create your views here.
# Home Page
def home(request):
    return render(request, 'LegoMyApp/lego_home.html')  # renders home page, no context

#View function that controls the main index page - list of Lego sets
def index(request):
    get_lego_sets = LegoSet.LegoSets.all()              # gets Lego sets currently in the database
    context = {'lego_sets': get_lego_sets}               # creates a dictionary object of lego sets for template
    return render(request, 'LegoMyApp/lego_index.html', context)

#View function that controls the main index page - list of MiniFigs
def index_mini(request):
    get_minifigs = MiniFig.MiniFigs.all()              # gets minifigs currently in the database
    context = {'minifigs': get_minifigs}                    # creates a dictionary object of minifigs for template
    return render(request, 'LegoMyApp/minifig_index.html', context)

#View function to add a new Lego set to the database
def add_lego_set(request):
    form = LegoSetForm(request.POST or None, request.FILES or None)     # Gets the posted form, if one exists
    if form.is_valid():                                                 #Checks the form for errors, to make sure it's filled in
        form.save()                                                      #Saves the valid form to the database
        return redirect('list_lego_sets')
    else:
        print(form.errors)                               #Prints any errors for the posted form to the terminal
        form = LegoSetForm()                             #Creates a new blank form
    return render(request, 'LegoMyApp/lego_create.html', {'form': form})

#View function to add a new minifig to the database
def add_minifig(request):
    form = MiniFigForm(request.POST or None, request.FILES or None)     # Gets the posted form, if one exists
    if form.is_valid():                                                 #Checks the form for errors, to make sure it's filled in
        form.save()                                                      #Saves the valid form to the database
        return redirect('list_minifigs')
    else:
        print(form.errors)                               #Prints any errors for the posted form to the terminal
        form = MiniFigForm()                             #Creates a new blank form
    return render(request, 'LegoMyApp/minifig_create.html', {'form': form})

def delete_lego_set(request, pk):
    pk = int(pk)
    lego_set = get_object_or_404(LegoSet, pk=pk)
    if request.method == 'POST':
        lego_set.delete()
        return redirect('list_lego_sets')
    context = {"lego_set": lego_set}
    return render(request, 'LegoMyApp/lego_delete.html', context)       # Confirm delete

def delete_minifig(request, pk):
    pk = int(pk)
    minifig = get_object_or_404(MiniFig, pk=pk)
    if request.method == 'POST':
        minifig.delete()
        return redirect('list_minifigs')
    context = {"minifig": minifig}
    return render(request, 'LegoMyApp/minifig_delete.html', context)       # Confirm delete

def deleted(request,pk):
    pk = int(pk)
    if request.method == 'POST':
        form = LegoSetForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.delete()
            return redirect('list_lego_sets')
    else:
        return redirect('list_lego_sets')

def deletedToo(request,pk):
    pk = int(pk)
    if request.method == 'POST':
        form = MiniFigForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.delete()
            return redirect('list_minifigs')
    else:
        return redirect('list_minifigs')

#View function to look up the details of a lego_set
def lego_details(request, pk):
    pk = int(pk)                                          #Casts value of pk to an int so it's in the proper form
    lego_set = get_object_or_404(LegoSet, pk=pk)          #Gets single instance of the lego_set from the database
    context={'lego_set':lego_set}                         #Creates dictionary object to pass the lego_set object
    return render(request,'LegoMyApp/lego_details.html', context)

#View function to look up the details of a minifig
def minifig_details(request, pk):
    pk = int(pk)                                          #Casts value of pk to an int so it's in the proper form
    minifig = get_object_or_404(MiniFig, pk=pk)          #Gets single instance of the lego_set from the database
    context={'minifig': minifig}                         #Creates dictionary object to pass the lego_set object
    return render(request,'LegoMyApp/minifig_details.html', context)

#Edit name, category or image of lego set
def lego_edit(request, id):
    id = int(id)
    lego_set = get_object_or_404(LegoSet, id=id)
    form = LegoSetForm(request.POST or None, request.FILES or None, instance=lego_set)
    if form.is_valid():
        form.save()
        return redirect('list_lego_sets')
    return render(request, 'LegoMyApp/lego_edit.html', context={'form': form,})

def api_response(request):
    location = get_user_location()
    lat= location['lat']
    lon= location['lon']
    weather= get_weather(lat, lon)
    return render(request, 'LegoMyApp/weather_api.html', weather, location)

