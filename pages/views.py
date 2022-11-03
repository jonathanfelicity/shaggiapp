from django.shortcuts import render

def home(req):
    return render(req, 'home.html')


def exchange(req):
    return render(req, 'exchange.html')

def converter(req):
    return render(req, 'converter.html')


def chart(req):
    return render(req, 'chart.html')


def contacts(req):
    return render(req, 'contact.html')