from django.core.validators import MinValueValidator
from rest_framework import serializers

from core.models import Question


class QuestionsCreateRequest(serializers.ModelSerializer):
    questions_num = serializers.IntegerField(
        help_text="Number of questions to be added.",
        validators=[MinValueValidator(0)]
    )

    class Meta:
        model = Question
        fields = [
            "questions_num"
        ]
