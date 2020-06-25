from django.forms import ModelForm
from .models import LegoSet
from .models import MiniFig

#Create the form class.
class LegoSetForm(ModelForm):
    class Meta:
        model = LegoSet
        fields = '__all__'

class MiniFigForm(ModelForm):
    class Meta:
        model = MiniFig
        fields = '__all__'