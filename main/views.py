from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('about')  # Додайте URL для сторінки успішної реєстрації
  else:
    form = RegistrationForm()

  return render(request, 'main/register.html', {'form': form})



def index(request):
  data = {
    'title': 'Головна сторінка',
  }

  return render(request,'main/index.html', data)

def about(request):
  return render(request,'main/about.html')

def contacts(request):
  return render(request,'main/contacts.html')
