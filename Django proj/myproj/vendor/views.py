from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .forms import SignupForm
# Create your views here.
from stores.models import Category, Stores
def index(request):
    store = Stores.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'vendor/index.html', {
        'categories': categories,
        'stores': store,
    })


def signup(request):
    if request.method == 'POST':
       form = SignupForm (request.POST)

       if form.is_valid():
           form.save()

           return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'vendor/signup.html', {
        'form': form
    })