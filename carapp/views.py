from django.views import View
from .models import CarType, LabGroupMember, Vehicle
from django.shortcuts import get_object_or_404, render
from .forms import OrderVehicleForm, SearchVehicleForm


# Create your views here.
def homepage(request):
    cartype_list = CarType.objects.all().order_by('id')
    return render(request, 'carapp/homepage.html', {'cartype_list': cartype_list})


def aboutus(request):
    return render(request, 'carapp/aboutus.html', {'about_us': 'This is a Car Showroom'})


def cardetail(request, cartype_no):
    context = {}
    i = get_object_or_404(CarType, pk=cartype_no)
    context['cartype_no'] = cartype_no
    resp = Vehicle.objects.filter(car_type=i)
    context['vehicles'] = resp
    return render(request, 'carapp/cardetail.html', context)


class GroupView(View):  # Have to define Class only once and all the related get and post methods can be defined under it.
    def get(self, request):  # get is defned
        members = LabGroupMember.objects.all()
        context = {}
        context['members'] = members
        return render(request, 'carapp/groupview.html', context)

    # seperate post method for GroupView can also be defined here as def post()


class VehiclesView(View):
    def get(self, request):
        context = {}
        context['vehicles'] = Vehicle.objects.all()
        return render(request, 'carapp/vehicles.html', context)


class OrderView(View):
    def get(self, request):
        context = {}
        context['order_form'] = OrderVehicleForm()
        return render(request, 'carapp/order.html', context)

    def post(self,request):
        context = {}
        order_form = OrderVehicleForm(request.POST)
        context['order_form'] = order_form
        return render(request,'carapp/order.html',context)

class SearchVehicle(View):
    def get(self,request):
        context={}
        context['search_vehicle_form'] = SearchVehicleForm()
        return render(request,'carapp/searchvehicle.html', context)

    def post(self,request):
        context={}
        search_vehicle_form= SearchVehicleForm(request.POST)
        if search_vehicle_form.is_valid():
            car_price = Vehicle.objects.get(car_name=search_vehicle_form.cleaned_data['vehicle']).car_price
            context['search_vehicle_form'] = search_vehicle_form
            context['car_price'] = car_price
        return render(request,'carapp/searchvehicle.html',context)