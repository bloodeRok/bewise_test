from typing import Any

from core.models import Question


class QuestionRepository:
    model = Question

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
                {'id': 1, 'question': 'What is...?', 'answer': 'The answer', 'value': 5, ...}, \n
                {'id': 2, 'question': 'How ...?', 'answer': 'Another answer', 'value': 10, ...}, \n
                ...
            ] \n
            new_questions = bulk_create(questions_data)
        """

        return self.model.objects.bulk_create(
            [
                Question(
                    id=question["id"],
                    text=question["question"],
                    answer=question["answer"],
                    value=question["value"],
                    created_at=question["created_at"],
                    updated_at=question["updated_at"]
                )
                for question in questions

            ]
        )

    def get_all_ids(self) -> list[int]:
        """
        Retrieves a list of all question IDs from the database.
        """

        return [query[0] for query in self.model.objects.values_list("id")]
