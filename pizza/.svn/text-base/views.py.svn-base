from estagio.pizza.models import *
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

def tipo_usuario(user):
    id = user.id
    try:
        empresa = Empresa.objects.get(id=id)
        return empresa, 'empresa'
    except:
        pass
    try:
        avaliador = Avaliador.objects.get(id=id)
        return avaliador, 'avaliador'
    except:
        pass
    try:
        aluno = Aluno.objects.get(id=id)
        return aluno, 'aluno'
    except:
        pass
    return None, None

class StatsForm(ModelForm):
    class Meta:
        model = UserStats

class TermoForm(ModelForm):
    class Meta:
        model = Termo
        fields = ['aluno','data_inicio','data_fim','empresa','valor_bolsa','funcao']
        
class TermoEditForm(ModelForm):
    #aluno = forms.ChoiceField(widget=forms.Select(attrs={'readonly':'readonly'}))
    class Meta:
        model = Termo
        fields = ['aluno', 'empresa', 'aprovado']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25,widget=forms.widgets.PasswordInput())
    
@login_required
def cria_termo(request):
    if request.method == 'POST':
        form = TermoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TermoForm()
    return render_to_response('termo.html', {'form': form})

class EmpresaForm(ModelForm):
	class Meta:
		model = Empresa
        
#@login_required
def cadastra_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmpresaForm()
    return render_to_response('cadastroEmpresa.html', {'form': form})
	
@login_required
def avalia_termo(request):
    contexto = RequestContext(request)
    user, tipo = tipo_usuario(contexto['user'])
    print str(user)
    print str(tipo)
    if tipo == 'avaliador':
        #tosqueira wins
        contexto['aprovacoes'] = Termo.objects.filter(empresa__avaliador=user)
    else:    
        contexto['aprovacoes'] = Termo.objects.all() #filter(empresa__avaliador__username='Avaliador1')#filter(aprovado='False')#
    return render_to_response('avaliaTermo.html', contexto)

@login_required
def edita_termo(request, codigo_termo):
	termo = Termo.objects.get(id=codigo_termo)
	if request.method == 'POST':
		form = TermoEditForm(request.POST, instance=termo)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/termo/list/')
	else:
		form = TermoEditForm(instance=termo)
	return render_to_response('termo.html', {'form': form})
    
@login_required
def welcome_page(request):
    contexto = RequestContext(request)
    form = ModelForm
    contexto['form'] = form
    return render_to_response('sistemaestagios.html', contexto)
    
def autenticacao(request):
    contexto = RequestContext(request)
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print str(user)
            if user is not None:
                login(request, user)
                print 'cai aqui'
                return HttpResponseRedirect('/sistemaestagios/')
    else:
        form = LoginForm()
    contexto['form'] = form
    return render_to_response('login.html', contexto)
    
def deslogar(request):
    logout(request)
    return render_to_response('logout.html')
    return HttpResponseRedirect('/sistemaestagios/')

#def welcome_page(request):
#    form = ModelForm
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(username=username, password=password)
#    if user is not None:
#        if user.is_active:
#            login(request, user)
#            # Redirect to a success page.
#        else:
#            return render_to_response('sistemaestagios.html', {'form': form})