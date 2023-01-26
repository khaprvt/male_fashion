from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import BlogModel
from django.views.generic import ListView, DetailView, CreateView
from .forms import CommentForm

# Create your views here.

class BlogListView(ListView):
    template_name = 'main/blog.html'
    paginate_by = 6
    
    
    def get_queryset(self):
        qs = BlogModel.objects.order_by('-id')
        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tags=tag)
        return qs
    
    
class BlogDetailView(DetailView):
    template_name = 'main/blog-details.html'
    model = BlogModel
    # context_object_name = 'blog'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    
class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'main/blog-details.html'
    
    def form_valid(self, form):
        blog = get_object_or_404(BlogModel, pk=self.kwargs.get('pk'))
        form.instance.blog = blog
        form.instance.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('blogs:detail', kwargs={'pk': self.kwargs.get('pk')})