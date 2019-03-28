from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import WishPost

class WishForm(ModelForm):
  class Meta:
    model = WishPost
    fields = ["id", "description", "quantity"]

def wish_list(request, template_name='mainapp/wish_list.html'):
  wishes = WishPost.objects.all()
  data = {}
  data['object_list'] = wishes
  return render(request, template_name, data)


def wish_create(request, template_name='mainapp/wish_form.html'):
  form = WishForm(request.POST or NONE)
  if form.is_valid():
    form.save()
    return redirect('mainapp:wish_list')
  return render(request, template_name, {'form': form})

def wish_update(request, pk, template_name='mainapp/wish_form.html'):
  wish = get_object_or_404(WishPost, pk=pk)
  form = WishForm(request.POST or NONE, instance=wish)
  if form.is_valid():
    form.save()
    return redirect('mainapp:wish_list')
  return render(request, template_name, {'form': form})

def wish_delete(request, pk, template_name='mainapp/wish_delete.html'):
  wish = get_object_or_404(WishPost, pk=pk)
  if request.method=='POST':
    wish.delete()
    return redirect('mainapp:wish_list')
  return render(request, template_name, {'object': wish})