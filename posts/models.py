from django.db import models

'''ORM - это Objective relational mapping '''

"""object.all() - возвращает QuerySet из всех обьектов модели"""
"""Comment.objects.get(text = '123') - возвращает один обьект модели с определенным id"""

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    image = models.ImageField(upload_to = "posts_images/", null = True, blank = True)
    title = models.CharField(max_length = 100)
    rate = models.IntegerField(default=0, max_length= 10)
    content = models.TextField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag, related_name = "posts")


    def __str__(self):
        return f'{self.title} - {self.rate}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "comments")#related_name = comments_set
    text = models.CharField(max_length=300)


