# coding=utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class GroupChat(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Чат группы'
        verbose_name_plural = 'Чаты групп'


class Message(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    group = models.ForeignKey(GroupChat, on_delete=models.CASCADE, verbose_name='Группа')
    text = models.CharField(max_length=500, verbose_name='Текст')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
