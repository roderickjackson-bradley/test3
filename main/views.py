from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import Wish

class WishForm(ModelForm):
  class Meta:
    model = Wish
    fields = ["id", "description", "quantity"]

def wish_list(request, template_name='main/wish_list.html'):
  wishes = Wish.objects.all()
  data = {}
  data['object_list'] = wishes
  return render(request, template_name, data)
