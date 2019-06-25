from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import BlogPost



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
    return 


def blog_post_create_view(request):
    return 

def blog_post_retrieve_view(request):
    return 

def blog_post_update_view(request):
    return 

def blog_post_delete_view(request):
    return 
