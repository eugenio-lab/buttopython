from django.shortcuts import render
import requests


def button(request):
	return render(request,'home.html')

def output(request):
	
	data=requests.get("https://www.google.com/")
	#print('Ti amo! <3')
	data=data.text
	data2='Ti Amo! <3'
	return render(request,'home.html',{'data':data2})


