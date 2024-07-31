import random

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from posts.models import Post, Tag
from posts.forms import PostForm, SearchForm, PostForm2
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
"""HttpResponse - текстовый ответ на запрос"""

#posts = ["post1", "post2", "post3", "post4", "post5", "post6", "post7", "post8", "post9", "post10" ...........]
#limit = 5
#posts_per_page = posts / limit


#Example 1:
#page = 1, limit = 5
#start = (1 - 1) * 5 = 0
#end = 1 * 5 = 5

#Example 2:
#page = 5, limit = 2
#( 5 - 1 ) * 2 = 8
# 5 * 2 = 10

class TestView(View):
    def get(self, request):
        return HttpResponse(f"Hello World{random.randint(0, 100)}")


def main_page(request):
    if request.method == "GET":
        print(request.user)

        return render(request, "main.page.html")


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts" #context = {'posts: post.objects.all()"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, }
        # dictionary["6"] = 6
        context["search_form"] = SearchForm
        return context


@login_required(login_url="login")
def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()  # (QuerySet)
        #list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        #indexes = list[2:6]
        limit = 4
        max_pages = posts.count() / limit
        # if round(max_pages) < max_pages:
        #     max_pages = round(max_pages) + 1
        # else:
        #     max_pages = round(max_pages)
        # # print(request.GET)
        page = int(request.GET.get("page", 1))
        search = request.GET.get("search")
        tag = request.GET.get("tag")
        ordering = request.GET.get("orderings")

        if search and len(search)>=1:
            posts = posts.filter(title__icontains = search)
        if tag:
            posts = posts.filter(tag__name__in=[tag])
        if ordering:
            print(ordering)
            posts = posts.order_by(ordering)
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        start = (int(page) - 1) * limit
        end = page * limit
        posts_per_page = posts[start:end]
        print(max_pages)
        for i in range(1, max_pages +1):
            print(i)
        form = SearchForm(request.GET)
        context = {"posts": posts, "search_form": form, "max_pages":range(1,max_pages+1), "page":page, "posts_per_page": posts_per_page}
        return render(request = request, template_name= "post_list.html", context = context )

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail_view.html"
    context_object_name = "post"
    lookup_url_kwarg = "post_id"


@login_required(login_url="login")
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


class PostCreateView(CreateView):
    model = Post
    template_name ="posts/post_create.html"
    form_class = PostForm2
    success_url ='/posts/'

    def get(self, request, *args, **kwargs):
        form = self.get_from()
        return self.render_to_response(self.get_template_names(), {'form': form})


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

