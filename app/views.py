from django.shortcuts import render, redirect
from .models import VoteUser
from datetime import datetime

# Create your views here.
def signin(request):
    # authenticate (Se connecter)

  
    return render(request, 'authentication/index2.html')


def election(request):
    # election
   
  
    return render(request, 'authentication/election.html')


def adhesion_aff(request):
    # adhsion
   
  
    return render(request, 'authentication/adhesion_aff.html')


def adhesion_codefo(request):
    # adhsion
   
  
    return render(request, 'authentication/adhesion_codefo.html')

def rencontre(request):
    # adhsion
   
  
    return render(request, 'authentication/rencotre.html')


def vote(request):
 
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = "test@test.com"
        telephone = request.POST['telephone']

        
        if request.POST['choix'] == "1" :
            choix = "jean"

        elif request.POST['choix'] == "2" :
            choix = "jacque"

        elif request.POST['choix'] == "3" :
            choix = "pierre"
        
        elif request.POST['choix'] == "0":
            choix = "Vote blanc"

        
        updated_at = datetime.now()

        record = VoteUser(
            first_name = fname,
            last_name = lname,
            email = email,
            telephone = telephone,
            choix = choix,
            updated_at = updated_at
        )

        record.save()
       

    return redirect("/signup")


def dashboard(request):
    

    return render(request, 'dashboard/index.html')

def all_users(request):
    

    return render(request, 'dashboard/all_users.html')



def signup(request):
    # authenticate (Se connecter)
    
   return render(request, 'authentication/index2.html')

