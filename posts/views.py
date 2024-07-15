from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post


def posts_view(request):
    posts = Post.objects.all() #(QuerySet)
    return render(request = request, template_name= "post_list.html", context ={"posts": posts} )


def posts_text_view(request):
    posts = Post.objects.all()
    return HttpResponse("Hello World ! Our posts would be here!")


def post_detail_view(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, 'post_detail_view.html', {'post': post})

def main_page(request):
    return render(request, "main.page.html")