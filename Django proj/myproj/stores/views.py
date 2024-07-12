from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .forms import NewStore, EditStore
from .models import Category, Stores

def stores(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    stores = Stores.objects.filter(is_sold=False)

    if category_id:
        stores = stores.filter(category_id=category_id)

    if query:
        stores = stores.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'stores/stores.html', {
        'stores': stores,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),

    })

def detail(request, pk):
    store = get_object_or_404(Stores, pk=pk)
    related_stores = Stores.objects.filter(category=store.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'stores/detail.html', {
        'store': store,
        'related_stores': related_stores
    })

def itemdetail(request, pk):
    item = get_object_or_404(Stores, pk=pk)
    related_stores = Stores.objects.filter(category=store.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'stores/itemdetail.html', {
        'store': item,
        'related_stores': related_stores
    })

#@login_required
def new(request):
    if request.method == 'POST':
        form = NewStore(request.POST, request.FILES)

        if form.is_valid():
            store = form.save(commit=False)
            store.created_by = request.user
            store.save()

            return redirect('stores:detail', pk=store.id)
    else:
        form = NewStore()

    return render(request, 'stores/form.html' , {
        'form': form,
        'title': 'Add store',
        
    })

@login_required
def delete(request, pk):
    store = get_object_or_404(Stores, pk=pk, created_by=request.user)
    store.delete()

    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    store = get_object_or_404(Stores, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditStore(request.POST, request.FILES, instance=store)

        if form.is_valid():
            form.save()

            return redirect('stores:detail', pk=store.id)
    else:
        form = EditStore(instance=store)

    return render(request, 'stores/form.html' , {
        'form': form,
        'title': 'Edit store',
        
    })