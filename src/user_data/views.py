from django.shortcuts import render, get_object_or_404, redirect
from .forms import *	
# Create your views here.
def home_view(request):
	return render(request,'User/home.html',{})

def user_create_view(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = UserForm()
	context = {
		'form' : form
	}
	return render(request,'User/user_create.html',context)

def user_list_view(request):
	queryset = User.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request,"User/user_list.html",context)

def user_details_view(request, user_id):
	obj = get_object_or_404(User,id=user_id)
	context = {
		'object' : obj
	}
	return render(request,'User/user_details.html',context)

def user_delete_view(request, user_delete_id):
	obj = get_object_or_404(User,id=user_delete_id)
	if request.method == "POST":
		get_object_or_404(User,id=user_delete_id).delete()
		return redirect('../../../../home')
	context = {
		"object" : obj
	}
	return render(request, 'User/user_delete.html',context)

def user_update_view(request, user_update_id):
	obj = get_object_or_404(User, id=user_update_id)
	form  = UserForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect('../../../../home')
	context = {
		"form" : form
	}
	return render(request, 'User/user_update.html' , context)