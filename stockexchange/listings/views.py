from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html",
                  {'bands': bands})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html',
                  {'listings': listings})


def contact(request):
    return HttpResponse("<h1> Nous contacter</h1> <p>Vous pouvez nous joindre via .... </p>")