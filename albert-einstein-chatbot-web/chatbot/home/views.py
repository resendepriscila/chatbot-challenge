from django.shortcuts import render

# Create your views here.
def home(request):
	titulo = 'HOME'
	return render(request, 'home.html', {'titulo': titulo})
