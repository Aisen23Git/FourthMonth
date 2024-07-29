from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from posts.models import Post
from posts.forms import PostForm, SearchForm
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



def main_page(request):
    if request.method == "GET":
        print(request.user)

        return render(request, "main.page.html")


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

