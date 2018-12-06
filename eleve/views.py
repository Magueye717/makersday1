from django.shortcuts import render, redirect
from .models import Eleve

# Create your views here.
def index(request):
    all_student = Eleve.objects.all()
    return render(request, 'eleve/index.html', {'all_student': all_student})

def create(request):
    print('page demande--------------------------------->>>>>')
    print(student)
    student=Eleve(nom_complet=request.POST['nom_complet'], 
                niveau_etude=request.POST['niveau_etude'],
                serie=request.POST['serie'])
    student.save()
    return redirect('/')