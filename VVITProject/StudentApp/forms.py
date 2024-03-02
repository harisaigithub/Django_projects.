from django import forms
from .models import StReg

class StForm(forms.ModelForm):
    class Meta:
        model = StReg
        fields = ["srn","sname","syear","sbranch"]
        widgets = {
            "srn":forms.TextInput(attrs={
              "placeholder":"Roll Number","class":"form-control my-2", 
            }),
            "sname":forms.TextInput(attrs={
              "placeholder":"Enter Name",
              "class":"form-control my-2",
            }),
            "syear":forms.NumberInput(attrs={
              "class":"form-control my-2",
              "max":4,
              "min":1,
            }),
            "sbranch":forms.Select(attrs={
              "class":"form-control my-2",
            }),
        }
