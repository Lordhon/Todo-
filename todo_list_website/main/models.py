from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']


# Сигналы для автоматического обновления кэша
@receiver(post_save, sender=Task)
def update_cache_on_save(sender, instance, **kwargs):
    """
    Обновление кэша при сохранении задачи (создание или изменение).
    """
    cache_key = f'tasks_user_{instance.user.id}'
    tasks_query = Task.objects.filter(user=instance.user)
    cache.set(cache_key, tasks_query, timeout=60 * 5)


@receiver(post_delete, sender=Task)
def update_cache_on_delete(sender, instance, **kwargs):
    """
    Очистка кэша при удалении задачи.
    """
    cache_key = f'tasks_user_{instance.user.id}'
    cache.delete(cache_key)




















