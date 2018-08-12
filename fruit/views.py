# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Fruit
from django.views.generic import ListView
from django.shortcuts import render,get_object_or_404

class Fruit_list(ListView):

    model = Fruit
    context_object_name = 'fruits'
    template_name = "fruit/fruit_list.html"

#class Blog_page(ListView):

    #model = Blog
    #context_object_name = 'blog'
    #template_name = "blog/blog_page.html"

def fruit_page(request, pk=None):
    fruit = get_object_or_404(Fruit.objects, pk=pk)
    return render(request, 'fruit/fruit_page.html', {'fruit': fruit})
# Create your views here.