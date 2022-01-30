from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from django.views.generic.base import View

URL = "http://127.0.0.1:8000/myapp/"


class ListView(View):
    def get(self, request, *args, **kwargs):
        r = requests.get(url=URL)
        context = r.json()
        print(context)
        return render(request, "myapp2/list.html", {"data":context})


class DetailView(View):
    def get(self, request, *args, **kwargs):
        id=kwargs['pk']
        ur = "http://127.0.0.1:8000/myapp/"+str(id)
        print(ur)
        r = requests.get(url=ur)
        context = r.json()
        print(context)
        return render(request, "myapp2/detail.html", {"data": context})
