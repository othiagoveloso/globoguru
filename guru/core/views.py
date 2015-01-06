#coding:utf-8 
from django.shortcuts import render
from guru.core.models import  Modulo, Training, Step
#from guru.subscriptions.models import Subscription 
from django.contrib.auth.models import User
from guru.home.models import Spotlight
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
#from django.shortcuts import render_to_response
#from django.contrib.auth import authenticate, logout, login as authlogin
#from django.template import RequestContext
from django.contrib.auth.decorators import login_required





@login_required
def home(request, template_name='index.html'):
    destaque = Spotlight.objects.all() 
    training = Training.objects.all()
    return render(request, template_name, {'Spotlight':destaque,'training':training})


def home_training(request, template_name='index.html'):
    training = Training.objects.get(id) 
    return render(request, template_name,{ 'training':training})


@login_required
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

@login_required
def modulo(request,slug):
     modulos = Modulo.objects.get(Modulo, slug=slug)
     context = { 'modulos': modulos }
     return render(request, 'modulos.html', context)


@login_required
def voltar_modulo(request,slug):
     
     modulos = Modulo.objects.get(slug=slug)
     training = Modulo.objects.get(trainings_id=modulos)
     etapas = Step.objects.filter(id=training)
     context = { 'training': etapas }
     return render(request, 'modulos.html', context)     

@login_required
def modulos(request,slug,template_name='modulos.html'):
    
    list_training = Training.objects.get(slug=slug)
    modulos = Modulo.objects.filter(trainings_id=list_training.id)
    return render(request, template_name, { 'modulos':modulos, 'title':modulos[0],'titles':modulos } )


def training_name(request,slug,template_name='modulos.html'):
    
    list_training = Training.objects.get(slug=slug)
    data = {}
    data['object_list'] = list_training

    return render(request, template_name, data )    


@login_required
def etapas(request,slug,template_name='etapas.html'):
    
    
    list_modulo = Modulo.objects.get(slug=slug)
    steps = Step.objects.filter(modulos_id=list_modulo)
    modulos = Modulo.objects.filter(trainings_id=list_modulo.trainings_id)

    
    
    proximo_modulo = ""
    
    
    count = 0
    quantidade = len(modulos)

    for mod in modulos:
        if count < quantidade-1:
            count = count+1

        if mod == list_modulo:
            proximo_modulo = modulos[count]

        
                
    

               
           

                
    return render(request, template_name,{'quantidade':quantidade, 'proximo_modulo':proximo_modulo.slug, 'steps':steps, 'title':steps[0],'movie':list_modulo.video})







@login_required
def video(request,id, template_name='etapas.html'):

    step = Step.objects.get(id=id)
    list_modulo = Modulo.objects.get(id=step.modulos_id)
    
    modulos = Modulo.objects.filter(trainings_id=list_modulo.trainings_id)
    proximo_modulo = ""
    
    count = 0
    quantidade = len(modulos)

    for mod in modulos:
        if count < quantidade-1:
            count = count+1

        if mod == list_modulo:
            proximo_modulo = modulos[count]

    



    steps = Step.objects.filter(modulos_id=list_modulo)

    
    return render(request, template_name,{'quantidade':quantidade, 'proximo_modulo':proximo_modulo.slug, 'movie':step.video, 'steps':steps, 'title':steps[0], 'step':step })    
    

@login_required
def aovivo(request, template_name='ao-vivo.html'):
    training = Training.objects.all()
    
    return render(request, template_name,{'Training':training})


def videovivo(request,slug, template_name='ao-video.html'):
    movies = Training.objects.get(slug=slug)
    training = Training.objects.all()
    
    
    return render(request, template_name, {'movie':movies.video,'Training':training,'object':movies})


def novidades(request,slug, template_name='novidades.html'):
    movies = Training.objects.get(slug=slug)
    training = Training.objects.all()
    
    
    return render(request, template_name, {'movie':movies.video,'Training':training,'object':movies})



def login(request, template_name="login2.html"):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) # Veja a documentacao desta funcao
        
        if form.is_valid():
            #se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
            #agora, basta logar o usuario e ser feliz.
            User(request, form.get_user())
            return HttpResponseRedirect("/?next=%s") # redireciona o usuario logado para a pagina inicial
        else:
            return render(request, "login2.html", {"form": form})
    
    #se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, template_name, {"form": AuthenticationForm()})







def logout(request, template_name="logout.html"):

    
    return render(request, template_name,)


@login_required
def voltar(request,slug,template_name='modulos.html'):
    
    list_training = Training.objects.get(slug=slug)
    modulos = Modulo.objects.filter(trainings_id=list_training.id)
    return render(request, template_name, { 'modulos':modulos.slug, 'title':modulos[0],'titles':modulos } )



