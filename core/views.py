from django.http import response
from django.shortcuts import render
import requests

def NigeriaStateList(request):
    response = requests.get("https://covidnigeria.herokuapp.com/api").json()
    context = {'response':response}
    return render(request, 'core.html', context)