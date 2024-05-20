from django import forms

class CarForm(forms.Form):
    car_name = forms.CharField(max_length=50)
    car_manufacturer = forms.CharField(max_length=50)
    car_year = forms.IntegerField()
    car_price= forms.FloatField()
    car_engine = forms.CharField(max_length=10)
class SearchForm(forms.Form):
    car_name = forms.CharField(max_length=50)