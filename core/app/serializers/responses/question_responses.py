from rest_framework import serializers

from core.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            "id",
            "text",
            "answer",
            "value",
            "created_at",
            "updated_at"
        ]
