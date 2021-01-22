from django import forms
from .models import Measurement

class MeasurementModelForm(forms.Form):
    location = forms.CharField()
    meal = forms.CharField()
# class MeasurementModelForm(forms.ModelForm):
#     class Meta:
#         model = Measurement
#         fields = ('location', 'destination',)
