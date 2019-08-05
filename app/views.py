from django.shortcuts import render
from .models import *
import json
import requests

url = 'http://127.0.0.1:8000/api_post'

# Create your views here.
def index(request):
	post = Post.objects.all()
	context = {
		'post':post,
	}
	return render(request,'index.html',context)

def detail(request, id):
	post = Post.objects.get(id=id)
	context = {
		'post':post,
	}
	return render(request,'detail.html',context)

def parse(request):
	variable_request = requests.get(url).text
	diction = json.loads(variable_request)
	print(diction)
	context = {
		'diction':diction,
	}
	return render(request, 'parse.html',context)