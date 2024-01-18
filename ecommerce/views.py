from django.shortcuts import render
from customadmin.models import GlobalSettings

# Create your views here.

def home(request):
    glob = GlobalSettings.objects.all()
    return render(request, "ecomm/main/home/home.html", {'glob':glob})
