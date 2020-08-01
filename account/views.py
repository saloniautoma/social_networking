from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView,DetailView,DeleteView
from django.views.generic import TemplateView
# Create your views here.
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView,DetailView,DeleteView
# Create your views here.

def ahome(request):
    context={}
    template = 'ahome.html'
    return render(request, template, context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('account:user_list')

    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, 'reg_form.html', args)

# class-based user list to find friends
class UserList(ListView):
    template_name = 'user_list.html'
    context_object_name = 'r'

    def get_queryset(self):
        return User.objects.all()

# to delete user-profil



'''def userlist(request):
    user = User.objects.all()
    query = request.GET.get('q')
    if query:
        user = user.filter(
            Q(city__icontains=query)
        ).distunct()
    context = {'users':user}
    template = 'user_list.html'
    return render(request,template,context)
'''
@login_required
def userdetail(request,id=None):
    instance = get_object_or_404(User, id=id)
    context = {'r':instance}
    template = 'user_detail.html'
    return render(request,template,context)

@login_required
def profile(request):
    context = {'user':request.user}
    template = 'profile.html'
    return render(request,template,context)



@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('account:profile')
    else:
        form = UserChangeForm(instance=request.user)
        context = {'form':form}
        template = 'edit_profile.html'
        return render(request,template,context)

@login_required
def changepassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form':form}
        template = 'change_password.html'
        return render(request,template,context)


@login_required
def deleteprofile(request,id = None):
    dal = get_object_or_404(User, id = id)
    dal.delete()
    context = {'msg':"Account Successfully deleted."}
    return render(request,'logout.html',context)