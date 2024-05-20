from django.shortcuts import render
from mycar.forms import CarForm, SearchForm
from mycar.models import carmodel
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'base.html')


def register(request):
    title = "New Registration"
    ack = "Registered Successfully"
    form = CarForm(request.POST or None)
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["car_name"]
            manufacturer = form.cleaned_data["car_manufacturer"]
            year = form.cleaned_data["car_year"]
            price = form.cleaned_data['car_price']
            engine = form.cleaned_data['car_engine']
            p = carmodel(car_name=name, car_manufacturer=manufacturer, car_year=year, car_price=price,
                         car_engine=engine)
            p.save()
            return render(request, 'ack.html', {'ACK': ack})
    return render(request, 'new.html', {'form': form, 'title': title})


def display(request):
    title = "All Registered Cars"
    queryset = carmodel.objects.all()
    context = {
        "title": title,
        "queryset": queryset
    }
    return render(request, 'display.html', context)


def search(request):
    title = "Search Car"
    form = SearchForm(request.POST or None)
    if form.is_valid():
        c_name = form.cleaned_data["car_name"]
        queryset = carmodel.objects.filter(car_name=c_name)
        if len(queryset) == 0:
            return render(request, 'ack.html', {"ACK": "Car not found"})
        context = {
            'title': title,
            'queryset': queryset,

        }
        return render(request, 'display.html', context)
    return render(request, 'search.html', {'form': form, 'title': title})
def delete(request):
    title = "Remove Car"
    ack = "Removed Successfully"
    form = SearchForm(request.POST or None)
    if form.is_valid():
        c_name = form.cleaned_data["car_name"]
        queryset = carmodel.objects.filter(car_name=c_name)
        if len(queryset) == 0:
            return render(request, 'ack.html', {"ACK": "Car not found"})
        else:
            queryset = carmodel.objects.filter(car_name=c_name).delete()
        return render(request,'ack.html',{"ACK":ack})
    return render(request, 'delete.html', {'form': form, 'title': title})
