from django.shortcuts import render, get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
from django.http import HttpResponse
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Create your views here.
def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)

    geolocator = Nominatim(user_agent="resturants")

    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        print(destination.address)
        d_lat = destination.latitude
        d_lon = destination.longitude
        pointA = (d_lat, d_lon)

        location_ = form.cleaned_data.get('location')
        print(location_)
        location = geolocator.geocode(location_, exactly_one=False)
        # print('<<<')
        # print(location)
        for i in location:
            print('>>>>')
            print(i.latitude)
            print(i.longitude)
            l_lat = i.latitude
            l_lon = i.longitude
        pointB= (l_lat, l_lon)
        # l_lat = location.latitude
        # l_lon = location.longitude
        distance = round(geodesic(pointA, pointB).km, 2)
        print('BBBBBBBBBBBBBB')
        print(distance)
        instance.destination = destination_
        instance.location = location_
        instance.distance = distance
        instance.save()

    context = {
        'distance': obj,
        'form': form,
    }

    return render(request, 'measurements/main.html', context)
