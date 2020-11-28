from django.shortcuts import render
from bikes_app.models import Bikes, BikeDetails
# Create your views here.

def bikesHome(request):
    bikes = Bikes.objects.all()
    bikes_dict = {'bikes':bikes}
    return render(request, 'bikes_app/bikes_home.html', context = bikes_dict)

def bikeDetails(request, id):
    # print(str(id))
    bike = Bikes.objects.get(id=id)
    # print(str(bike.variant))
    bikeDetails = BikeDetails.objects.get(bike=bike)
    # print(bikeDetails.engine_type)


    # bikes = Bikes.objects.all()
    # bikes_dict = {'bikes':bikes}
    return render(request, 'bikes_app/bike_details.html', {"bike_details":bikeDetails})
