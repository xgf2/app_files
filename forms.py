from django import forms
from files.models import User

#class IdentifierData(forms.Form):
#    identifier = forms.CharField(label = ' Identifier ', max_length = 100)
#    code = forms.CharField(label = ' Code ', max_length = 100)

class IdentifierData(forms.ModelForm):
    class Meta:
        model = User
        fields = ['identifier', 'code']

