from django.forms import ModelForm, fields
from app.models import Youdo_Medo

class Youdo_Medo_Form(ModelForm):
    class Meta:
        model = Youdo_Medo
        fields = ['title', 'status', 'priority']
        