from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm



# GET -> 1 object
# Filter -> [] objects


def blog_post_detail_page(request, slug):
    # print(post_id.__class__())
    # obj = BlogPost.objects.get(slug=slug)   -> 1object
    obj = get_object_or_404(BlogPost, slug=slug)
    # queryset = BlogPost.objects.filter(slug=slug)

    # if queryset.count() == 0:
    #     raise Http404
    # obj = queryset.first()
      # try:
    #     obj = BlogPost.objects.get(slug=slug)
    # except BlogPost.DoesNotExist:
    #     raise Http404
    # except ValueError:
    #     raise Http404
    template_name = "blog_post_detail_page.html"
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    # list of view
    # could be search
    now = timezone.now()

    #qs = BlogPost.objects.all()  # list of python objects
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    #qs = BlogPost.objects.filter(publish_date__lte=now)
    #qs = BlogPost.objects.filter(title__icontains='hello') # could be a search
    template_name = 'blog/post_list.html'
    context = {'objects_list': qs}
    return render(request, template_name, context)

# @login_required()
@staff_member_required
def blog_post_create_view(request):
        # create objects
    # ? use a form
    # request.user -> return something 
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # obj.title = form.cleaned_data.get("title") + "0"
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = 'blog/form.html'
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # get details of single object
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)
    
@staff_member_required
def blog_post_update_view(request, slug):    
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'blog/form.html'
    context = {'title': f"Update {obj.title}", 'form': form}
    return render(request, template_name, context)
  
@staff_member_required
def blog_post_delete_view(request,slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {'object': obj}
    return render(request, template_name, context)
    
