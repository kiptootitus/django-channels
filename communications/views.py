from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
@login_required
def chat_view(request):
  chat_group = get_object_or_404(ChatGroup, group_name ='test')
  chat_messages = chat_group.chat_messages.all()[:30]
  form = chatMessageCreateForm()
  if request.htmx:
        form = chatMessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                'message' : message,
                'user' : request.user
            }
            return render(request, 'comm/partials/chat_message_p.html', context)
      
  
  return render(request, 'comm/chat.html', {'chat_messages': chat_messages, 'form': form})