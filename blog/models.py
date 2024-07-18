from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name="заголовок")
    body = models.TextField(verbose_name="содержание")
    image = models.ImageField(upload_to="blog", verbose_name="изображение", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(default=True, verbose_name="признак публикации")
    views_count = models.PositiveIntegerField(default=0, verbose_name="количество просмотров")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name="владелец")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"