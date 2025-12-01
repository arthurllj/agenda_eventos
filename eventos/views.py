from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Evento
from .forms import EventoForm

def evento_list(request):
    busca = request.GET.get('q')
    if busca:
        eventos = Evento.objects.filter(titulo__icontains=busca)
    else:
        eventos = Evento.objects.all()
    return render(request, 'evento_list.html', {'eventos': eventos})

def evento_detail(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, 'evento_detail.html', {'evento': evento})

@login_required
def evento_create(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventos:evento_list')
    else:
        form = EventoForm()
    return render(request, 'evento_form.html', {'form': form})
