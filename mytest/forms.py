from django import forms


def addForm(forms.Form):
    a = forms.IntegerField(primary_key=True)
    b = forms.IntegerField(primary_key=True)