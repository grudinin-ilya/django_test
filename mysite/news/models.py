from django.db import models

class News (models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True) # blank = True не обящательно к заполнению
    created_at = models.DateTimeField(auto_now_add=True) # дата создания контента не будет изменяться
    updated_at = models.DateTimeField(auto_now=True) # дата будет изменяться
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True) # контент по умолчанию публикуется

    def __str__(self):
        return self.title
