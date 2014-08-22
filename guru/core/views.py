from django.shortcuts import render
from guru.core.models import  Modulo, Training, Step
from guru.home.models import Spotlight



def home(request, template_name='index.html'):
    destaque = Spotlight.objects.all() 
    data = {}
    data['object_list'] =  destaque
    return render(request, template_name, data)

def home_training(request, template_name='index.html'):
    training = Training.objects.all() 
    data = {}
    data['object_list'] =  training
    return render(request, template_name, data)


def treinamento(request, template_name='treinamentos.html'):
    training = Training.objects.all()
    data = {}
    data['object_list'] = training
    return render(request, template_name, data)

def treinamentos_plataforma(request, template_name='treinamentos_plataforma.html'):
    training = Training.objects.all()
    data = {}
    data['object_list'] = training
    return render(request, template_name, data)    

def treinamentos_produto(request, template_name='treinamentos_produto.html'):
    training = Training.objects.all()
    data = {}
    data['object_list'] = training
    return render(request, template_name, data)      

def modulo(request,slug):
     modulos = Modulo.objects.get(Modulo, slug=slug)
     context = { 'modulos': modulos }
     return render(request, 'modulos.html', context)


def modulos(request,slug,template_name='modulos.html'):
    
    list_training = Training.objects.get(slug=slug)
    modulos = Modulo.objects.filter(trainings_id=list_training)
    return render(request, template_name, { 'modulos':modulos, 'title':modulos[0] } )


def training_name(request,slug,template_name='modulos.html'):
    
    list_training = Training.objects.get(slug=slug)
    data = {}
    data['object_list'] = list_training

    return render(request, template_name, data )    



def etapas(request,slug,template_name='etapas.html'):
    
    list_modulo = Modulo.objects.get(slug=slug)
    steps = Step.objects.filter(modulos_id=list_modulo)
    
    
    return render(request, template_name,{ 'steps':steps, 'title':steps[0],'movie':list_modulo.video})




def video(request,id, template_name='etapas.html'):

    step = Step.objects.get(id=id)
    list_modulo = Modulo.objects.get(id=step.modulos_id)
    steps = Step.objects.filter(modulos_id=list_modulo)

    
    return render(request, template_name,{ 'movie':step.video, 'steps':steps, 'title':steps[0], 'step':step })    
    


def aovivo(request, template_name='ao-vivo.html'):
    training = Training.objects.all()
    
    return render(request, template_name,{'Training':training})


def videovivo(request,slug, template_name='ao-vivo-video.html'):
    movies = Training.objects.get(slug=slug)
    training = Training.objects.all()
    
    
    return render(request, template_name, {'movie':movies.video,'Training':training})



