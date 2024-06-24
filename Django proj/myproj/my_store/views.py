from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.
from stores.models import Stores

@login_required
def index(request):
    stores = Stores.objects.filter(created_by=request.user)

    return render(request, 'my_store/index.html', {
        'stores': stores,
    })


