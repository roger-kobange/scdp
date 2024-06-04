from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views.generic import ListView,CreateView
from .models import User_c, Machine, Technicien
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict


from .forms import *

from .models import Article, User_c

def accueil(request):
    articles = Article.objects.all()
    return render(request, 'accueil.html', {'articles': articles})

def dashboard(request):

    return render(request, 'dashboard.html')

def login_views(request, *args, **kwargs):
   
    return render(request, 'login.html')
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('/')
        else:
            messages.warning(request, "Username or Password is incorrect !!")
            return redirect('/accounts/login/')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/accounts/login/')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            form = SignUpForm(request.POST)
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

class UserForm(forms.ModelForm):
    class Meta:
        model = User_c 
        fields = '__all__' 
        


def machine_list(request):
    machines = Machine.objects.all()
    form = MachineForm()  # Créez une instance du formulaire
    return render(request, 'machine_list.html', {'machines': machines, 'form': form})

def create_machine(request):
    if request.method == "POST":
        form = MachineForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Machine créée avec succès!")
                return redirect('/machines/')
            except:
                messages.error(request, "Quelque chose s'est mal passé lors de la création de l'agence!")
    else:
        form = MachineForm()  # Si la requête n'est pas POST, créez simplement une nouvelle instance du formulaire

    return render(request, 'machine_list.html', {'form': form})

    
class CreateMachineView(CreateView):
    model = Machine
    form_class = MachineForm
    template_name = 'machine_list.html'  # Utilisez le même template ou un différent si nécessaire
    success_url = '/machines/'  # Modifiez selon vos besoins

    
def user_list(request):
    users = User_c.objects.all()
    form = User_cForm()  # Créez une instance du formulaire
    return render(request, 'machine_list.html', {'users': users, 'form': form})
   
def technicien_list(request):
    techniciens = Technicien.objects.all()
    form = TechnicienForm()  # Créez une instance du formulaire
    return render(request, 'machine_list.html', {'techniciens': techniciens, 'form': form})

def create_technicien(request):
    if request.method == "POST":
        form = TechnicienForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Technicien créée avec succès!")
                return redirect('/techniciens/')
            except:
                messages.error(request, "Quelque chose s'est mal passé lors de la création de l'agence!")
    else:
        form = TechnicienForm()  # Si la requête n'est pas POST, créez simplement une nouvelle instance du formulaire

    return render(request, 'technicien_list.html', {'form': form})


def edit_machine(request, id):
    machine = get_object_or_404(Machine, id=id)
    form = MachineForm(instance=machine)
    form_data = model_to_dict(form.instance)  # Convertir l'instance de modèle en dictionnaire
    return JsonResponse(form_data)

def update_machine(request, id):
    client = get_object_or_404(Machine, id=id)
    form = MachineForm(request.POST or None, request.FILES or None, instance=client)
    if form.is_valid():
        form.save()
        messages.success(request, 'Client mis à jour avec succès!')
        return redirect('/machines/')
    return render(request, 'pages/client/client.html', {'form': form, 'client': client})

def delete_machine(request, id):
    client = get_object_or_404(Machine, id=id)
    client.delete()
    messages.success(request, 'La machine a été supprimé avec succès!')
    return redirect('/machines/')