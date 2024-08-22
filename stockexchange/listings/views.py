from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("<h1> Hello Django !</h1>")


def about(request):
    return HttpResponse("<h1> A propos</h1> <p>Nous aimons la bourse de marchandises</p>")


def listings(request):
    return HttpResponse("<h1> Ci après la liste des  marchandises</h1> "
                        "<p><ul> <li> Element1</li> <li> Element2</li></ul></p>")


def contact(request):
    return HttpResponse("<h1> Nous contacter</h1> <p>Vous pouvez nous joindre via .... </p>")