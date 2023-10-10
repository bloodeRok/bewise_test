from typing import Any

from core.models import Question


class QuestionRepository:
    model = Question

    def create(
            self,
            external_id: int,
            text: str,
            answer: str,
            value: int,
            created_at: str,
            updated_at: str
    ) -> Question:
        """
        Creates a new Question object in the database.
        """

        new_question = self.model.objects.create(
            id=external_id,
            text=text,
            answer=answer,
            value=value,
            created_at=created_at,
            updated_at=updated_at
        )

        return new_question

    def bulk_create(
            self,
            questions: list[dict[str, Any]]
    ) -> list[Question]:
        """
        Creates multiple Question objects in the database.

        Args:
            questions (list[dict[str, Any]]): A list of dictionaries containing question information.
                Each dictionary should have keys 'id', 'question', 'answer', 'value', 'created_at', and 'updated_at'.

        Returns:
            list[Question]: A list of newly created Question objects.

        Example usage:
            questions_data = [
                {'id': 1, 'question': 'What is...?', 'answer': 'The answer', 'value': 5, ...},
                {'id': 2, 'question': 'How does...?', 'answer': 'Another answer', 'value': 10, ...},
                ...
            ]
            new_questions = bulk_create(questions_data)
        """

        new_questions = []
        for question in questions:
            new_question = self.create(
                external_id=question["id"],
                text=question["question"],
                answer=question["answer"],
                value=question["value"],
                created_at=question["created_at"],
                updated_at=question["updated_at"]
            )
            new_questions.append(new_question)

        return new_questions

    def get_all_ids(self) -> list[int]:
        """
        Retrieves a list of all question IDs from the database.
        """

        return [query[0] for query in self.model.objects.values_list("id")]
