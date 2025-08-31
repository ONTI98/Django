from django.views.generic import TemplateView   
from .models import Post
from django.views.generic import DetailView 


class HomeView(TemplateView):
    template_name="home.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['posts']=Post.objects.all()
  
        return context
    
class PostDetailView(DetailView):
    model=Post
    template_name="details.html"
    context_object_name="post"
