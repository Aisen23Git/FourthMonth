from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from posts.models import Post
from posts.forms import PostForm
"""HttpResponse - текстовый ответ на запрос"""


@login_required(login_url="login")
def main_page(request):
    if request.method == "GET":
        print(request.user)

        return render(request, "main.page.html")


def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all() #(QuerySet)
        return render(request = request, template_name= "post_list.html", context ={"posts": posts} )


def posts_text_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return HttpResponse("Hello World ! Our posts would be here!")


def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id = post_id)
        return render(request, 'post_detail_view.html', {'post': post})

def main_page(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "main.page.html", {'form': form})


def post_create_view(request):
    if request.method == "GET":
        return render(request, 'post_create.html')
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'post_create.html', {'form': form})
        # title = request.POST.get("title")
        # content = request.POST.get("content")
        # image = request.FILES.get("image")
            title = form.cleaned_data.get("title")
            # request.Post.get("content")
            content = form.cleaned_data.get("content")
            image = form.cleaned_data.get("image")
            print(image, title, content)

            post = Post.objects.filter(title=title, content=content)
            if not post:
                Post.objects.get_or_create(title = title, content = content, image = image)
                return redirect("posts")
            return HttpResponse("Такой пост уже существует")

