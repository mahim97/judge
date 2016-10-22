from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import question



def index(request):
	que=question.objects.order_by('sub')
	return render(request, 'ques/list.html',{'que': que})
def detail(request, prob_code):
    question1 = get_object_or_404(question, pk=prob_code)
    return render(request, 'ques/detail.html', {'question2': question1})
	
 
