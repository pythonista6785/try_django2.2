from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
	my_title = "Hello there..."
	context = {"title": "Hello there.."}

	template_name = "title.txt"
	template_obj = get_template(template_name)
	rendered_string = template_obj.render(context)

	return render(request,"hello_world.html", {"title": rendered_string})

def about_page(request):
	return render(request,"about.html", {"title": "about"})

def contact_page(request):
	return render(request, "hello_world.html", {"title": "about"})


def example_page(request):
	context = {"title": "Example"}
	template_name = "hello_world.html"
	template_obj = get_template(template_name)
	rendered_item = template_obj.render(context)
	return HttpResponse(rendered_item)