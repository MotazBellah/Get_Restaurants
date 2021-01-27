from django import forms


class MeasurementModelForm(forms.Form):
    location = forms.CharField()
    meal = forms.CharField()
