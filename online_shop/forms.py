from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import kategorija, umetnicko_delo, naracka, posetitel_na_aplikacijata


class KategorijaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(KategorijaForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = kategorija
        exclude = ("user",)

class UmetnickoDeloForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UmetnickoDeloForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = umetnicko_delo
        exclude = ("user",)

class NarackaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NarackaForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = naracka
        exclude = ("user",)



class RegisterForm(forms.ModelForm):

    class Meta:
        model = posetitel_na_aplikacijata
        exclude=("user",)

        widgets ={

     'ime': forms.TextInput(attrs={'class': 'form-control'}),
     'prezime': forms.TextInput(attrs={'class': 'form-control'}),
     'e_mail_adresa': forms.TextInput(attrs={'class': 'form-control'}),
      'username': forms.TextInput(attrs={'class': 'form-control'}),
      'password': forms.TextInput(attrs={'class': 'form-control'}),
      'telefonski_broj': forms.TextInput(attrs={'class': 'form-control'}),

        }

    class MyAuthenticationForm(AuthenticationForm):
        username = forms.CharField(max_length=150)
        password = forms.CharField(max_length=12)

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }