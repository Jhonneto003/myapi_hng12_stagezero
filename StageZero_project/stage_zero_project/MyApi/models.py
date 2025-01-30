# from django.db import models
# from django.utils import timezone

# # Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=50)
#     email= models.EmailField()
#     registered_at= models.DateTimeField(default=timezone.now())
#     github_url = models.URLField(max_length= 100, null=True, blank=True)

#     def __str__(self):
#         return self.name