from django.forms.widgets import ChoiceWidget
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from random import choice
from django.db.models import F 
from RockPaperScissor.forms import NameForm,MoveForm
from core.models import Player,Rounds
from django.urls import reverse
from django.db.models import Sum



CHOICE=['R','P','S']

class PlayView(TemplateView):
    template_name='core/play.html'
    def get(self,*args,**kwargs):
        return render(self.request,"core/play.html")
    def post(self,*args,**kwargs):
        if(self.request.Method=='POST'):
            p=Player.objects.get(id=self.request.session['PlayerId'])
            player_round=Rounds.objects.filter(Name=p)
            player_round.delete()
            b=Player.objects.get(id=self.request.session['BotId'])
            bot_round=Rounds.objects.filter(Name=b)
            bot_round.delete()
        return render(self.request,'core/play.html')



count=0


class RoundView(ListView):
    model=Rounds
    template_name='core/round.html'
    def get(self,*args,**kwargs):
        form=MoveForm()
        Name_qs=Player.objects.get(id=self.request.session['PlayerId'])
        p=Player.objects.get(id=self.request.session['PlayerId'])
        player_round=Rounds.objects.filter(Name=p)
        b=Player.objects.get(id=self.request.session['BotId'])
        bot_round=Rounds.objects.filter(Name=b)
        self.request.session['player_points']=player_round.aggregate(Sum('Score'))
        self.request.session['bot_points']=bot_round.aggregate(Sum('Score'))
        

        return render(self.request,"core/round.html",{'form':form,'player_round':player_round,'bot_round':bot_round,'name_object':Name_qs})

    def post(self,*args,**kwargs):
        context={}
        form=MoveForm()
        context['form']=form
        global count
        print(self.request.method)
        if (self.request.method=='POST'):

            
            
            count=count+1
            self.request.session['count']=count
            form=MoveForm(self.request.POST)
            bot_move=choice(CHOICE)
            


            if (form.is_valid()):
                
                
                form.save(commit=False)
                if(form.cleaned_data['Move']=='P'):
                    if bot_move == 'R':
                        q1=Player.objects.get(id=self.request.session['PlayerId'])
                        b1=Player.objects.get(id=self.request.session['BotId'])
                        Rounds.objects.create(Name=b1,Move='R',Score=0)
                        Rounds.objects.create(Name=q1,Move='P',Score=1)
                        self.request.session['response'] = "Bot has chosen rock.You Win "
                        print("1")

                    elif bot_move == 'S':
                        q1=Player.objects.get(id=self.request.session['PlayerId'])
                        Rounds.objects.create(Name=q1,Move='P',Score=0)
                        b1=Player.objects.get(id=self.request.session['BotId'])
                        Rounds.objects.create(Name=b1,Move='S',Score=1)
                        self.request.session['response'] = "Bot has chosen scissors.You lose. "
                        print("2")
                    

                    elif bot_move == 'P':
                        q1=Player.objects.get(id=self.request.session['PlayerId'])
                        Rounds.objects.create(Name=q1,Move='P',Score=0)
                        b1=Player.objects.get(id=self.request.session['BotId'])
                        Rounds.objects.create(Name=b1,Move='P',Score=0)
                        self.request.session['response'] = "Bot has chosen paper as well. It's a tie "
                        print("3")
                        
                    
                elif(form.cleaned_data['Move']=='S'):

                    if bot_move == 'P':
                        q1=Player.objects.get(id=self.request.session['PlayerId'])
                        Rounds.objects.create(Name=q1,Move='S',Score=1)
                        b1=Player.objects.get(id=self.request.session['BotId'])
                        Rounds.objects.create(Name=b1,Move='P',Score=0)
                        self.request.session['response'] = "Bot has chosen paper.You win"
                        print("4")


                    elif bot_move == 'R':
                        q1=Player.objects.get(id=self.request.session['PlayerId'])
                        Rounds.objects.create(Name=q1,Move='S',Score=0)
                        b1=Player.objects.get(id=self.request.session['BotId'])
                        Rounds.objects.create(Name=b1,Move='R',Score=1)
                        self.request.session['response'] = "Bot has chosen rock.You lose "
                        print("5")

                    elif bot_move == 'S':
                        q1=Player.objects.get(id=self.request.session['PlayerId'])
                        Rounds.objects.create(Name=q1,Move='S',Score=0)
                        b1=Player.objects.get(id=self.request.session['BotId'])
                        Rounds.objects.create(Name=b1,Move='S',Score=0)
                        self.request.session['response'] = "Bot has chose scissors as well. It's a tie "
                        print("6")

                elif(form.cleaned_data['Move']=='R'):

                    if bot_move == 'P':
                        q1=Player.objects.get(id=self.request.session['PlayerId'])
                        Rounds.objects.create(Name=q1,Move='R',Score=0)
                        b1=Player.objects.get(id=self.request.session['BotId'])
                        Rounds.objects.create(Name=b1,Move='P',Score=1)
                        self.request.session['response'] = "Bot has chosen paper.You lose"
                        print("7")

                    elif bot_move == 'S':
                        q1=Player.objects.get(id=self.request.session['PlayerId'])
                        Rounds.objects.create(Name=q1,Move='R',Score=1)
                        b1=Player.objects.get(id=self.request.session['BotId'])
                        Rounds.objects.create(Name=b1,Move='S',Score=0)
                        self.request.session['response'] = "Bot has chosen scissors.You win"
                        print("8")

                    elif bot_move == 'R':
                        q1=Player.objects.get(id=self.request.session['PlayerId'])
                        Rounds.objects.create(Name=q1,Move='R',Score=0)
                        b1=Player.objects.get(id=self.request.session['BotId'])
                        Rounds.objects.create(Name=b1,Move='R',Score=0)
                        self.request.session['response'] = "Bot has chosen rock as well. It's a tie "
                        print("9")
                if(count==5):
                    count=0
                    self.request.session['count']=count
                    print("10")
                    return redirect('core:round')

                else:
                    print("11")
                    return redirect('core:round')
        else:
            count=0
            self.request.session['count']=count
            print("12")
            return render(self.request,"core/round.html",context)

class results(TemplateView):
    template_name='core/h.html'

