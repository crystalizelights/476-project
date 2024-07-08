from django.shortcuts import render, get_object_or_404
from stores.models import Stores
from .models import Review
from .forms import ReviewTextForm
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


def review_new(request, stores_pk):
    stores = get_object_or_404(Stores, pk=stores_pk)

    # Redirect if the current user is the owner of the store
    if stores.created_by == request.user:
        return redirect('my_store:index')
    
    # Check if the user has already reviewed this store
    reviews = Review.objects.filter(stores=stores).filter(participants__in=[request.user.id])
    if reviews.exists():
        # You may want to handle this case differently (e.g., show a message)
        pass

    if request.method == 'POST':
        form = ReviewTextForm(request.POST)

        if form.is_valid():
            # Create a new Review instance for the store
            review = Review.objects.create(stores=stores)
            review.participants.add(request.user)
            review.participants.add(stores.created_by)
            review.save()

            # Save the review message associated with this review
            review_message = form.save(commit=False)
            review_message.review = review
            review_message.created_by = request.user
            review_message.save()

            # Redirect to store detail view after successful review submission
            return redirect('stores:detail', pk=stores_pk)
    else:
        form = ReviewTextForm()

    # Render the review form template with the form object
    return render(request, 'review_new.html', {'form': form})