from django import forms
from carapp.models import OrderVehicle, Buyer


class OrderVehicleForm(forms.ModelForm):
    buyer = forms.ModelChoiceField(queryset=Buyer.objects.all(), widget=forms.RadioSelect)
    number_of_vehicles_ordered = forms.IntegerField(label='Number of Vehicles Ordered')

    class Meta:
        model = OrderVehicle
        fields = ['vehicle', 'buyer', 'number_of_vehicles_ordered']


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=50)
    email = forms.EmailField(label='Email ID')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message')


class SearchVehicleForm(forms.ModelForm):
    class Meta:
        model = OrderVehicle
        fields = ['vehicle']
