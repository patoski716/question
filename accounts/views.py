from django.shortcuts import render, get_object_or_404,redirect
from .models import *
# from .forms import *
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,  login, logout
# from django.contrib import messages, auth
# from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    return render(request,'home.html')

def question(request):
    posts=Question.objects.order_by('-date_added')
    context={'posts':posts}
    return render(request,'question.html',context)

def search(request):
  posts = Question.objects.order_by('-date_added')
  if 'course_title' in request.GET:
      course_title = request.GET['course_title']
      if course_title:
          query = Question.objects.filter(course_title__icontains=course_title)
          
  context={'query':query,'posts':posts}
  return render(request,'search.html',context)