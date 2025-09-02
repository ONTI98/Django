from django.views.generic import TemplateView
from .models import Post
from django.views.generic import DetailView
from django.views.generic import FormView
from .forms import PostForm
from django.contrib import messages


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by(
            "-pk"
        )  # will arrange posts in descednding order

        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "details.html"
    context_object_name = "post"


class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/"  # This will take you back to the home page

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # create a new post
        new_post = Post.objects.create(
            text=form.cleaned_data["text"], image=form.cleaned_data["image"]
        )
        messages.add_message(
            self.request, messages.SUCCESS, "Post uploaded succesfully"
        )
        return super().form_valid(form)
