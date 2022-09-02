from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    #template = loader.get_template('foodapp\index.html')
    context = {
        "item_list": item_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'foodapp\index.html', context)

def item(request):
    return HttpResponse("<h1>This is an item view.</h1>")

def detail(request,item_id):
    item = Item.objects.get(pk= item_id)
    context = {
        "item": item,
    }
    return render(request, 'foodapp\detail.html', context)
    



