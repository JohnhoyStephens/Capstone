from django.shortcuts import render
from django.http import HttpRespone


# Create your views here.
def index(respone):
    return HttpRespone("<h1>Income Predictor</h1>")

