from django import forms


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
            raise forms.ValidationError("Название не может быть python")
        return self.cleaned_data
