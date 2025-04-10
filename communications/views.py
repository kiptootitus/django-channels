from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def chat_view(request):
  chat_group = get_object_or_404(ChatGroup, group_name ='test')
  chat_messages = chat_group.chat_messages.all()[:30]
  return render(request, 'comm/chat.html', {chat_messages: chat_messages})