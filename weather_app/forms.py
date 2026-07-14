from django import forms

class CitySearchForm(forms.Form):
    city_name=forms.CharField(max_length=100,label='Введіть місто',)