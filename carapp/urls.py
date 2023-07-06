from django.urls import path, re_path
from . import views

app_name = 'carapp'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('carapp/<int:cartype_no>/',views.cardetail, name='cardetail'), #as_view() method is not used to with views
    path('group/', views.GroupView.as_view(), name='group'),  # as_view() method is used to with views
    path('carapp/vehicles/',views.VehiclesView.as_view(),name='vehicles'),
    path('carapp/orderhere/', views.OrderView.as_view(), name='orderhere'),
    path('carapp/searchvehicle', views.SearchVehicle.as_view(),name='searchvehicle'),

]
