from audioop import reverse
from urllib import request

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from pyexpat.errors import messages

from . import forms
from .models import kategorija, umetnicko_delo, naracka, avtor, posetitel_na_aplikacijata
from .forms import KategorijaForm, UmetnickoDeloForm, NarackaForm, RegisterForm
from .models import kategorija
# Create your views here.

def home(request):
    return render(request, 'home.html')


def korisnici(request):

    korisnici_list=posetitel_na_aplikacijata.objects.all()
    return render(request, 'korisnici.html', {'korisnici_list':korisnici_list})

def kategorii(request):

    kategorija_list=kategorija.objects.all()
    return render(request, 'kategorii.html', {'kategorija_list':kategorija_list})

def umetnickiDela(request):

    umetnickiDela_list=umetnicko_delo.objects.all()
    return render(request, 'umetnickiDela.html', {'umetnickiDela_list':umetnickiDela_list})

def naracki(request):

    naracki_list=naracka.objects.all()
    return render(request, 'naracki.html', {'naracki_list':naracki_list})

def avtori(request):

    avtori_list=avtor.objects.all()
    return render(request, 'avtori.html', {'avtori_list':avtori_list})


def dodadiKategorija(request):
    if request.method == "POST":
        form_data = KategorijaForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            kategorija = form_data.save(commit=False)
            kategorija.ime_na_kategorija = form_data.cleaned_data["ime_na_kategorija"]

            kategorija.save()
            return redirect("kategorii")


    context = {"form": KategorijaForm}
    return render(request, "AddCategory.html", context=context)



def deleteCategory(request, id_na_kategorija):
 category = kategorija.objects.get(id_na_kategorija=id_na_kategorija)
 category.delete()
 return redirect('kategorii')

def dodadiUmetnickoDelo(request):

    if request.method == "POST":
        form_data = UmetnickoDeloForm(data=request.POST, files=request.FILES)

        if form_data.is_valid():
            umetnicko_delo = form_data.save(commit=False)

            umetnicko_delo.ime_na_umetnicko_delo = form_data.cleaned_data["ime_na_umetnicko_delo"]
            umetnicko_delo.dimenzija = form_data.cleaned_data["dimenzija"]
            umetnicko_delo.cena = form_data.cleaned_data["cena"]
            umetnicko_delo.slika_od_umetnicko_delo = form_data.cleaned_data["slika_od_umetnicko_delo"]
            umetnicko_delo.id_avtor = form_data.cleaned_data["id_avtor"]
            umetnicko_delo.id_na_kategorija=form_data.cleaned_data["id_na_kategorija"]

            umetnicko_delo .save()
            return redirect("umetnickiDela")

    queryset = avtor.objects.all()
    queryset2 = kategorija.objects.all()
    context = {"authors": queryset, "categories": queryset2 , "form": UmetnickoDeloForm}
    return render(request, "AddArtwork.html", context=context)



def dodadiNaracka(request):
    if request.method == "POST":
        form_data = NarackaForm(data=request.POST, files=request.FILES)

        if form_data.is_valid():
            naracka = form_data.save(commit=False)

            naracka.tip = form_data.cleaned_data["tip"]
            naracka.opis = form_data.cleaned_data["opis"]
            naracka.status = form_data.cleaned_data["status"]
            naracka.datum = form_data.cleaned_data["datum"]
            naracka.id_na_umetnicko_delo = form_data.cleaned_data["id_na_umetnicko_delo"]
            naracka.id_kupuvac = form_data.cleaned_data["id_kupuvac"]
            naracka.id_avtor = form_data.cleaned_data["id_avtor"]

            naracka.save()
            return redirect("naracki")


    queryset = umetnicko_delo.objects.all()
    queryset2 = avtor.objects.all()
    context = {"umtnicki_dela": queryset,"avtori":queryset2 ,"form": NarackaForm}
    return render(request, "AddOrder.html", context=context)

def Register(request):
    form_class = RegisterForm
    form = form_class(request.POST or None)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        return redirect('/kategorii')

    return render(request, "login.html", {})


def loginPage(request):
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')

           user = authenticate(username=username, password=password)
           if user is not None:
               login(request, user)
               messages.info(request, f"You are now logged in as {username}")
               return redirect('kategorii/')
           #else:
               #messages.error(request, "Invalid username or password.")

       #else:
          # messages.error(request, "Invalid username or password.")
   form = AuthenticationForm()
   return render(request=request, template_name="login.html", context={"login_form": form})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        posetitel_na_aplikacijata = authenticate(request, username=username, password=password)

        if posetitel_na_aplikacijata is not None:
            login(request, posetitel_na_aplikacijata)
            return redirect('home')
        else:
            print("Hello")
            return redirect('login')


    else:
        return render(request, 'login.html', {})