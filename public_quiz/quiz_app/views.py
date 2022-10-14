from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from .forms import SignUpForm,QuestionForm,LogInForm
from .models import Score,Questions
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin
# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "registration/sign_up.html"


class AddQuestionView(LoginRequiredMixin,SuperuserRequiredMixin,CreateView):
    form_class = QuestionForm
    template_name = 'quiz_app/add_question.html'
    success_url = reverse_lazy("add_question")
    
    

class LeaderBoardView(ListView):
    model = Score
    template_name = "quiz_app/leader_board.html"
    context_object_name = 'leader_board_list'

    def get_queryset(self):
        return Score.objects.order_by('-score')


@login_required(login_url=reverse_lazy('login'))
def quiz(request):
    if request.method == 'POST':
        questions=Questions.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            if q.answer ==  request.POST[q.question]:
                score+=1
                correct+=1
            else:
                wrong+=1
        if total !=0 : percent = score/(total) *100
        else: percent = 0

        s = Score(user = request.user,score = score)
        s.save()
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'quiz_app/result.html',context)
    else:
        questions=Questions.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz_app/quiz.html',context)   


class LogInView(LoginView):
    form_class = LogInForm

def log_out(request):
    logout(request)
    return redirect('/')
    
    