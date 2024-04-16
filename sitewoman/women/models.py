from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True) # Можно пропустить информацию, поставив True
    time_create = models.DateTimeField(auto_now_add=True) # Заполнение впемени атоматически при публикации
    time_update = models.DateTimeField(auto_now=True) # Изменяется время и дата при обнафылении инфы
    is_published = models.BooleanField(default=True) # Булево значение. По дефолту True

    def __str__(self):
        return self.title







