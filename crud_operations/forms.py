from django import forms
from .models import Info


class InfoForm(forms.ModelForm):
    class Meta:
        model=Info
        fields=['name','address','phone_number']
        widgets={
            'name':forms.TextInput(attrs={'id':'nameid'}),
            'address':forms.Textarea(attrs={'id':'addressid'}),
            'phone_number':forms.TextInput(attrs={'id':'phoneid'})
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) 

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control form-inline'   