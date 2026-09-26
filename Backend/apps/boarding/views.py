from django.shortcuts import render


def boarding_houses(request):
    return render(request, "boarding/boarding_houses.html")