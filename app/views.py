from django.shortcuts import render


# Create your views here.
def signin(request):
    # authenticate (Se connecter)

  
    return render(request, 'authentication/index.html')


def signup(request):
    # authenticate (Se connecter)
       
    return render(request, 'authentication/signup.html')

