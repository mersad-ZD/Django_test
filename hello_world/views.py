from django.shortcuts import render

def hello_world(requset):
    return render(requset,'hello_world.html',{})

