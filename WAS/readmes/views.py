from django.shortcuts import render

# Create your views here.
def craft(request):
    return render(request, 'craft.html')