from django.db import models

class Profile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

    logo = models.ImageField(upload_to='profile_images', blank=True)
    age = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.user.username