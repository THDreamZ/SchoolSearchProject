from django.db import models

class User(models.Model):
    UserName = models.CharField(max_length=128, unique=True)
    UserPassword = models.CharField(max_length=256)
    c_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.UserName
    
    class Meta:
        ordering = ['c_time']
        verbose_name = 'user'
        verbose_name_plural = 'user'
