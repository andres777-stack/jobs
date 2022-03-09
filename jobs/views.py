
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.urls import reverse
from acceso.models import User
from jobs.forms import JobForm
from jobs.models import Job


def index(request):
    if request.method == 'GET':
        if 'usuario' not in request.session:
            messages.error(request, 'No estás logeado')
            return redirect(reverse('acceso:index'))
        else:
            user = request.session['usuario']
            context = {
            'usuario' : User.objects.get(id = user['id']),
            'jobs' : Job.objects.exclude(state = True),
            }

            return render(request, 'jobs/index.html', context)

def add(request):
    if request.method == 'GET':
        if 'usuario' not in request.session:
            messages.error(request, 'No estás logeado')
            return redirect(reverse('acceso:index'))
        else:
            print(request.session['usuario'])
            user = request.session['usuario']
            context = {
            'formModel': JobForm(),
            'usuario' : User.objects.get(id = user['id']),
            
            }
            return render(request, 'jobs/form.html', context)
    
    if request.method == 'POST':
        print(request.POST)
        form = JobForm(request.POST)
        if form.is_valid():
            #hasta aquí sólo se están haciendo las validaciones
            usuario = request.session['usuario']
            print(usuario)
            id = usuario['id']
            #nombre = usuario['nombre']
            print(id)
            user = User.objects.get(id=id)
            print(user)
            job = Job.objects.create(
                title = form.cleaned_data['title'], 
                desc = form.cleaned_data['desc'],
                location = form.cleaned_data['location'],
                owner = user,
            )
            messages.success(request, 'Job añadido exitosamente')
            return redirect(reverse('jobs:index'))
        else:
            messages.error(request, 'Con errores, solucionar')
            return render(request, 'jobs/form.html', {'formModel'  : form})

def cancel(request, id):
    
    if request.method =='GET':
        if 'usuario' not in request.session:
            messages.error(request, 'No estás logeado')
            return redirect(reverse('acceso:index'))
        else:
            wish = Job.objects.get(id=id)
            wish.delete()
            return redirect(reverse('jobs:index'))

def edit(request, id):

    if request.method == 'GET':
        if 'usuario' not in request.session:
            messages.error(request, 'No estás logeado')
            return redirect(reverse('acceso:index'))
        else:
            job = Job.objects.get(id=id)
            form = JobForm(instance=job)

            context = {
                'formModel' : form,
            }

            return render(request, 'jobs/editar.html', context)
        
    if request.method == 'POST':
            print(request.POST)
            job = Job.objects.get(id=id)
            form = JobForm(request.POST, instance=job)
            if form.is_valid():
                    form.save()
                    messages.success(request, 'Job editado correctamente')
                    return redirect(reverse('jobs:index'))
            else:
                    messages.error(request, 'Con errores, solucionar')
                    return render(request, 'jobs/editar.html', {'formModel'  : form})

def ver(request, id):
    if request.method == 'GET':
        if 'usuario' not in request.session:
            messages.error(request, 'No estás logeado')
            return redirect(reverse('acceso:index'))
        else:
            job = Job.objects.get(id=id)
            context={
                'job': job,
            }
            return render(request, 'jobs/ver.html', context)

def adding(request, id):
    if request.method == 'GET':
        if 'usuario' not in request.session:
            messages.error(request, 'No estás logeado')
            return redirect(reverse('acceso:index'))
        else: 
            job = Job.objects.get(id=id)
            job.state = True
            user = request.session['usuario']
            inst_user = User.objects.get(id = user['id'])
            Job.objects.create(
                title = job.title,
                desc = job.desc,
                location = job.location,
                owner = inst_user,
                state = True,
            )
            job.delete()
            return redirect(reverse('jobs:index'))

    
            
# Create your views here.
