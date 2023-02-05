from django.shortcuts import render, redirect
from django.contrib import messages
from .models import VoteUser
from .models import User_rcsm
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
    Users = VoteUser.objects.all() 

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        telephone = request.POST['telephone']

        if request.POST['choix'] == "Fr" :
            choix = "France"

        elif request.POST['choix'] == "An" :
            choix = "Angleterer"

        elif request.POST['choix'] == "Bel" :
            choix = "Belgique"
        
        elif request.POST['choix'] == "Esp":
            choix = "Espagne"

        elif request.POST['choix'] == "Sui":
            choix = "Suisse"

        elif request.POST['choix'] == "other":
            choix = "other"

        try:
            if request.POST['chk[]'] == "on":
                status = True
        except Exception as e:
            status = False
        

        ville = request.POST['ville']

        adresse = request.POST['adresse']
        
        # for vote in Vote_Users:

        #     if vote.first_name == fname or vote.last_name == fname :
        #         messages.add_message(request, messages.INFO, 'Sorry ! Vous avez déja ')
        print(status)    
        record = VoteUser(
            first_name = fname,
            last_name = lname,
            telephone = telephone,
            choix = request.POST['choix'],
            ville = ville,
            adresse = adresse,
            status = status, 
            updated_at = datetime.now()
            # updated_at = updated_at
        )

        try:
            record.save()
            messages.add_message(request, messages.INFO, 'Well done! vous avez validé .')

        except Exception as e:
            messages.add_message(request, messages.INFO, 'Sorry ! Vous avez deja voté un candicat.')
            print('vous avez deja voté')
       

    return redirect("/signup")


def dashboard(request):

    Users = VoteUser.objects.all()

    total = Users.count()

    return render(request, 'dashboard/index.html', {'nombre':total})

def all_users(request):
    Users = VoteUser.objects.all()

    # for vote in Vote_Users:

        #     if vote.first_name == fname or vote.last_name == fname :
        #         messages.add_message(request, messages.INFO, 'Sorry ! Vous avez déja ')
        

    return render(request, 'dashboard/all_users.html', {'Users':Users})



def signup(request):
    # authenticate (Se connecter)
    
   return render(request, 'authentication/index2.html')

