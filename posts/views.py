from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post


def posts_view(request):
    posts = Post.objects.all()
    return render(request = request, template_name= "post_list.html")

def posts_text_view(request):
    # posts = Post.objects.all()
    return HttpResponse("Hello World ! Our posts would be here!")


def main_page(request):
    return render(request, "main.page.html")