import uuid

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField('created', auto_now_add=True)
    updated_at = models.DateTimeField('updated', auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Task(UUIDMixin, TimeStampedMixin):
    class TaskStatus(models.TextChoices):
        Added = 'added'
        Done = 'done'
        InProgress = 'in_progress'

    title = models.TextField('title', blank=False, unique=True)
    text = models.TextField('text', blank=True)
    status = models.TextField(
        'status', choices=TaskStatus.choices, default=TaskStatus.Added
    )
    users = models.ManyToManyField(User, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'content"."tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
