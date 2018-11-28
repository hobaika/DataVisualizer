from django import forms
from .models import Enterpise_Data

class TableForm(forms.ModelForm):
    class Meta:
        model = Enterpise_Data
        fields = ('tables', 'cats',)





    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)
      #  self.fields['city'].queryset = City.objects.none()