from django.shortcuts import render

# Create your views here.
def contactUs(request):
    return render(request, 'main_app/contact_us.html')
