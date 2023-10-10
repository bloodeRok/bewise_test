from django.urls import path

from core.app.handlers.question_handlers import questions

urlpatterns = [
    path(
        "",
        questions,
        name="questions"
    ),
]
