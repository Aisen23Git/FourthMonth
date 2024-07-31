from django import forms

from posts.models import Tag, orderings, Post


class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        title = self.cleaned_data.get("title")
        content = self.cleaned_data.get("content")
        if title.lower() == content.lower():
            raise forms.ValidationError("Заголовок и содержание не могут совпадать")
        return title
    
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title =="python":
            raise forms.ValidationError("Название не может быть 'python' ")
        return self.cleaned_data

class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        widgets = {
            'title':forms.TextInput(attrs = {'class': 'form-control', "placeholder": "Заголовок"}),
            'content': forms.Textarea(attrs={'class': 'form-control', "placeholder": "Текст"})
        }

    def clean(self):
        title = self.cleaned_data.get("title")
        content = self.cleaned_data.get("content")
        if title.lower() == content.lower():
            raise forms.ValidationError("Заголовок и содержание не могут совпадать")
        return title

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title == "python":
            raise forms.ValidationError("Название не может быть 'python' ")
        return self.cleaned_data


class SearchForm(forms.Form):
    search = forms.CharField(
        required= False,
        max_length=200,
        min_length=1,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Поиск'})
    )
    tag = forms.MultipleChoiceField(
        required = False,
        choices = Tag.objects.value_list('name','name'),
        widget=forms.CheckboxSelectMultiple
    )

    orederings = (
        ('title', 'По заголовку'),
        ("-title", "По заголовку в обратном порядке"),
        ('rate', 'По оценке'),
        ("-rate", "По оценке в обратном порядке"),
        ('created_at', 'По дате создания'),
        ("-created_at", "По дате создания в обратном порядке"),
    )

    ordering = forms.CharField(
        required = False,
        choices = orderings,
        widget= forms.Select(attrs={'class': 'form-control'})
    )