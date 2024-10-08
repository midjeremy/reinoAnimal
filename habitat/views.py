from django.shortcuts import render
import random
# Create your views here.


#Funcion del Estado de los animales del Zoologico
def estadoAnimal (request):
    #Listas
    animalList = ["Tigre", "Pinguino", "Jirafa", "Elefante"]
    estadoList = ["Buen Estado", "Mal Estado", "Aislamiento Social", "Enfermedad", "Coavalecencia"]
    
    #Se declara las Variables con la funcionalidad de Random y con sus respectivas listas
    animales = random.choice(animalList)
    age = random.randrange(1,11)
    estado = random.choice(estadoList)

    #Diccionario con los datos que solicitara la plantilla esta llamara a las variables previamente declaradas y seran utilizados por el template
    data = {"Animal" : animales,
            "Edad" : age,
            "Estado" : estado}
    
    #Se realiza la
    return render(request, 'ReinoATemplates/estadosAnimal.html', data)