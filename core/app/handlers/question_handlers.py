from django.http import JsonResponse
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)
from rest_framework.decorators import api_view
from rest_framework.request import Request

from core.app.api_exceptions import TooMuchAttempts
from core.app.serializers.requests import QuestionsCreateRequest
from core.app.serializers.responses import QuestionSerializer
from core.app.serializers.responses.error_serializer import APIErrorSerializer
from core.app.services import QuestionService


@extend_schema_view(
    post=extend_schema(
        tags=["questions"],
        operation_id="Adds Questions",
        description="Adds new unique questions to db.",
        request=QuestionsCreateRequest,
        responses={
            201: OpenApiResponse(
                response=QuestionSerializer(many=True),
                description=f"New unique questions."
            ),
            409: OpenApiResponse(
                response=APIErrorSerializer,
                description=f"No unique questions.",
                examples=[
                    OpenApiExample(
                        name="Too many attempts",
                        value={"detail": TooMuchAttempts.default_detail},
                        status_codes=[TooMuchAttempts.status_code],
                        response_only=True
                    )
                ]
            ),
        }
    )
)
@api_view(["POST"])
def questions(request: Request):
    data = QuestionsCreateRequest(data=request.data)
    data.is_valid(raise_exception=True)
    data = data.validated_data

    new_questions = QuestionService().add_questions(num=data["questions_num"])
    return JsonResponse(
        QuestionSerializer(new_questions, many=True).data,
        safe=False
    )
