from django.shortcuts import render, get_object_or_404, redirect
from .forms import MeasurementModelForm
from .find_resturants import findAResturant
from django.http import HttpResponse
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium

# Create your views here.
def calculate_distance_view(request):

    geolocator = Nominatim(user_agent="resturants")
    form = MeasurementModelForm(request.POST or None)
    resturants_list = []
    location_ = ''

    map_osm = ''
    if request.method == "POST":
        # If form ins valid, get the meal and location
        if form.is_valid():
            meal = form.cleaned_data.get('meal')
            location_ = form.cleaned_data.get('location')
            # Geocode the location
            location = geolocator.geocode(location_, exactly_one=False)
            # Make sure the location has a coordinate point
            for i in location:
                l_lat = i.latitude
                l_lon = i.longitude

            point = (l_lat, l_lon)
            # Get the resturants list
            resturants_list = findAResturant(meal, point)
            # Use the folium to ge the map, with marker
            map_osm = folium.Map(width='100%', height=550, location=[l_lat, l_lon], zoom_start=13)
            folium.Marker([l_lat, l_lon], tooltip="Click here for more", popup=location_, icon=folium.Icon(color='purple')).add_to(map_osm)
            # Loop through the list and get the latitude and longitude of the resturant and add the marker to folium map
            for i in resturants_list:
                popup_action = "<strong>" + i['name'] + "</strong><br>"
                folium.Marker([i['lat_lng'][0], i['lat_lng'][1]], tooltip="Click here for more", popup=popup_action, icon=folium.Icon(color='blue', icon='cloud')).add_to(map_osm)
        # Repesent the folium map to HTML
        map_osm = map_osm._repr_html_()

    context = {
        'form': form,
        'map': map_osm,
        'resturants': resturants_list,
        'location': location_,
    }

    return render(request, 'measurements/main.html', context)
