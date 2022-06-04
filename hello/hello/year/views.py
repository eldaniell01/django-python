import datetime
from django.shortcuts import render
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "year/index.html",{
        "year": now.month == 6 and now.day == 4
    })