from typing import Counter
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from .forms import NameForm
from core.models import Player

class HomeView(ListView):
    model=Player
    template_name="home.html"
    def get(self,*args,**kwargs):
        global Count
        count=0
        self.request.session['count']=count
        form=NameForm()    
        return render(self.request,"home.html",{'form':form})

    def post(self,*args,**kwargs):
        context={}
        form=NameForm()
        context['form']=form
        
        if self.request.method=='POST':
            form=NameForm(self.request.POST)
            
            if form.is_valid():
                p=Player(Name=form.cleaned_data['Name'])
                p.save()
                b=Player(Name='bot')
                b.save()
                self.request.session['PlayerId']=p.id
                self.request.session['BotId']=b.id
                self.request.session['count']=0
                self.request.session['bot_points']=0
                self.request.session['player_points']=0
                
                return redirect('core:play')
            return render(self.request,"home.html",context)  
