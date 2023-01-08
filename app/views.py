from django.shortcuts import render, redirect
from django.contrib import messages
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
    Vote_Users = VoteUser.objects.all()


    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        telephone = request.POST['telephone']

        
        if request.POST['choix'] == "1" :
            choix = "jean"

        elif request.POST['choix'] == "2" :
            choix = "jacque"

        elif request.POST['choix'] == "3" :
            choix = "pierre"
        
        elif request.POST['choix'] == "0":
            choix = "Vote blanc"

        
        for vote in Vote_Users:

            if vote.first_name == fname :
                print('exist')
                
    
        updated_at = datetime.now()

        record = VoteUser(
            first_name = fname,
            last_name = lname,
            telephone = telephone,
            choix = choix,
            # updated_at = updated_at
        )

        try:
            record.save()
            messages.add_message(request, messages.INFO, 'Well done! vous avez voté.')

        except Exception as e:
            messages.add_message(request, messages.INFO, 'Sorry ! Vous avez deja voté un candicat.')
            print('vous avez deja voté')
       

    return redirect("/signup")


def dashboard(request):

    Vote_Users = VoteUser.objects.all()

    total = Vote_Users.count()

    return render(request, 'dashboard/index.html', {'nombre':total})

def all_users(request):
    

    return render(request, 'dashboard/all_users.html')



def signup(request):
    # authenticate (Se connecter)
    
   return render(request, 'authentication/index2.html')

