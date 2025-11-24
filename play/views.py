from django.shortcuts import render, redirect
from . forms import RegisterForm
from .models import Hero, Paragraph

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            country = form.cleaned_data['country']
            age = form.cleaned_data['age']

            starting_paragraph = Paragraph.object.first()

            Hero.objects.create(
                name = name,
                email = email,
                country = country,
                age = age,
                current_paragraph = starting_paragraph
            )

            return redirect('game_start')

    else:
        form = RegisterForm()

    return render(request, contact.html, {'form':form})