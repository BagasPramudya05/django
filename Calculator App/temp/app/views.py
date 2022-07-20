from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
	return render(request,"calc.html",{})

def wordcalci(request):
	return render(request,"wordcalci.html",{})