from core.app.api_exceptions import TooMuchAttempts
from core.app.repositories import QuestionRepository
from core.app.services.helpers.api_connection import (
    fetch_questions_from_api
)
from core.models import Question


class QuestionService:
    repository = QuestionRepository()

    def add_questions(
            self,
            num: int,
            max_attempts: int = 100
    ) -> list[Question]:
        """
        Adds a specified number of unique questions to the database.

        Args:
            num (int): The number of unique questions to add.
            max_attempts (int, optional): The maximum number of attempts
             to fetch unique questions. Defaults to 100.

        Raises:
            TooMuchAttempts: If maximum attempts are reached and unique
             questions are not obtained.
        """

        unique_questions = []
        attempts = 1
        existing_question_ids = self.repository.get_all_ids()

        while len(unique_questions) < num:
            if attempts == max_attempts:
                raise TooMuchAttempts

            count = num - len(unique_questions)
            external_questions = fetch_questions_from_api(count=count)

            if not external_questions:
                break

            unique_external_questions = [
                question for question in external_questions
                if question["id"] not in existing_question_ids
            ]

            unique_questions.extend(unique_external_questions)

            attempts += 1

        new_questions = self.repository.bulk_create(questions=unique_questions)

        return new_questions
