# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from web.models import Message,Month,Menu
from django.template import RequestContext
from web.forms import MessageForm
from django.utils import timezone

def home(request):
  months = Month.objects.all().order_by("-id")
  return render_to_response('home.html', {'months': months}, context_instance=RequestContext(request))

def board(request):
  messages = Message.objects.all()
  # response_string = "Evaluation:"
  # response_string += '<br/>'.join(["$ %s: %s time:%s" % (q.user, q.subject, q.publication_date) for q in messages])
  return render_to_response('board.html',{'msgs': messages})

def post(request):
  if request.method == 'POST':
    form = MessageForm(request.POST)
    if form.is_valid():
      message = Message(user=form.cleaned_data['user'],subject=form.cleaned_data['subject'], publication_date=timezone.now())
      message.save()
      return redirect('/board')
  else:
      form = MessageForm()
  return render_to_response('post.html',{'form': form}, context_instance=RequestContext(request))

def menu(request):
  menu = Menu.objects.all()
  return render_to_response('menu.html',{'menu': menu})

  