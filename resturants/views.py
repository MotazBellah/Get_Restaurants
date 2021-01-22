from django.shortcuts import render, get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
from .find_resturants import findAResturant
from django.http import HttpResponse
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium

# Create your views here.
def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)

    geolocator = Nominatim(user_agent="resturants")

    map_osm = folium.Map(width=800, height=500, location=[45.5236, -122.6750])
    folium.Marker([45.5236, -122.6750], tooltip="Click here for more", popup="TEST", icon=folium.Icon(color='purple')).add_to(map_osm)

    if form.is_valid():
        # instance = form.save(commit=False)
        meal = form.cleaned_data.get('meal')
        location_ = form.cleaned_data.get('location')
        print(location_)
        location = geolocator.geocode(location_, exactly_one=False)
        for i in location:
            print('>>>>')
            # print(i.latitude)
            # print(i.longitude)
            l_lat = i.latitude
            l_lon = i.longitude
        point = (l_lat, l_lon)

        print('//////////////////////')
        print(point)
        print(meal)
        resturants_list = findAResturant(meal, point)
        print(resturants_list)

        map_osm = folium.Map(width=400, height=500, location=[l_lat, l_lon])
        folium.Marker([l_lat, l_lon], tooltip="Click here for more", popup=location_, icon=folium.Icon(color='purple')).add_to(map_osm)
        for i in resturants_list:
            folium.Marker([i['lat_lng'][0], i['lat_lng'][1]], tooltip="Click here for more", popup=i['name'], icon=folium.Icon(color='red', icon='cloud')).add_to(map_osm)

        # map_osm = folium.Map(width=800, height=500,location=pointA)
    map_osm = map_osm._repr_html_()

    context = {
        'distance': obj,
        'form': form,
        'map': map_osm,
    }

    return render(request, 'measurements/main.html', context)
