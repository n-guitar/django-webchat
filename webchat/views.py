from django.shortcuts import render
from django.views import generic


class WebChatTop(generic.TemplateView):
    template_name = 'webchat/top.html'
