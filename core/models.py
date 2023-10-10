from django.db import models


class Question(models.Model):
    id = models.AutoField(
        primary_key=True,
        help_text="Unique identifier for each question"
    )  # ID вопроса
    text = models.TextField(
        help_text="Body of the question."
    )  # Текст вопроса
    answer = models.TextField(
        help_text="Answer of the question."
    )  # Текст ответа
    value = models.IntegerField(
        help_text="Value of the question.",
        null=True
    )  # Ценность вопроса
    created_at = models.DateTimeField(
        help_text="Question creation date and time."
    )  # Дата создания вопроса
    updated_at = models.DateTimeField(
        help_text="Question last update date and time."
    )  # Дата последнего обновления вопроса

    def __repr__(self):
        return f"<Question(" \
               f"body={self.pk}, " \
               f"answer={self.answer}, " \
               f"value={self.value}, " \
               f"created_at={self.created_at}, " \
               f"updated_at={self.updated_at}" \
               f")>"

    def __str__(self):
        return self.__repr__()
