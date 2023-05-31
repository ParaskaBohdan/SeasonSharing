from multiprocessing import AuthenticationError
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms import formset_factory
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import *
from django.views.generic import *
from django.contrib.auth import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.views import LoginView
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


def index(request):
   return render(request, "login.html")


def show(request):
   return render(request, "blank.html")

class EventsView(ListView):
   model = Event
   template_name = "EventsView.html"
   context_object_name = 'events'
   
   def get_queryset(self):
      season = self.kwargs['season']
      querySet = super().get_queryset()
      querySet = querySet.filter(season__name = season)
      return querySet
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RegisterForm()
        context['Form'] = form
        context['season'] = 'season'
        return context

class EventView(ListView):
   model = Event
   template_name = "EventView.html"
   context_object_name = 'event'
   def get_queryset(self):
    title = self.kwargs['title']
    queryset = super().get_queryset()
    event = queryset.filter(name=title).first()
    if event is None:
        raise Http404("Event does not exist")
    return event

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RegisterForm()
        context['Form'] = form
        context['season'] = 'season'
        return context

def addEvent(request): 
    event = Event();
    if request.method == 'POST': 
        form = EventForm(request.POST, request.FILES, instance=event) 
        if form.is_valid(): 
            form.save() 
            return redirect('ShowEv') 
        else: 
            errors = form.errors 
            for field, error_msgs in errors.items(): 
                for error_msg in error_msgs: 
                    print(f"Помилка у полі {field}: {error_msg}") 
    else: 
        form = EventForm() 
     
    return render(request, "event_create.html", { 
        "events": event, 
        "form": form, 
        'authenticated' : request.user.is_authenticated, 
        'user' : request.user, 
    })

def edit(request, title): 
         
    book = Event.objects.filter(name=title).first() 
 
    if request.method == 'POST': 
        form = EventForm(request.POST, request.FILES, instance=book) 
        if form.is_valid(): 
            form.save() 
            # return redirect('edit', title=book.name) 
        else: 
            errors = form.errors 
            for field, error_msgs in errors.items(): 
                for error_msg in error_msgs: 
                    print(f"Помилка у полі {field}: {error_msg}") 
    else: 
        form = EventForm(instance=book) 
 
    return render(request, "event_create.html", { 
        "form": form, 
        "header": 'Редагувати книгу', 
        'authenticated' : request.user.is_authenticated, 
        'user' : request.user 
    })
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'Register.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
       user = form.save()
       login(self.request, user)
       return redirect('ShowEv')
   

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('ShowEv')


def logout_user(request):
    logout(request)
    return redirect('login')