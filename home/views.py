from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import homeForm
from .models import Post

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = homeForm()
        posts = Post.objects.all().order_by('created')
        context = {'form':form,'posts':posts}
        return render(request,self.template_name,context)

    def post(self,request):
        form = homeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = homeForm()
            return redirect('home:home')

        context = {'form':form, 'text':text}
        return render(request,self.template_name,context)