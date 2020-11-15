import random
from .models import Question


class QuestionGenerator:
    """
    Questions are imported dynamically from the Question model.  The Question model
    contains a module name and a class name.  First we import all question in the db
    and then we add the class names to the list of question_choices.
    """

    @staticmethod
    def question_factory(queryset):
        """
        Used to get a random question. Returns a random question instance
        from question_choices.
        """
        questions = queryset
        for question in questions:
            exec (f"from questions.questions.{question.module_name} import {question.class_name}")
        question_choices = questions.values_list('class_name', flat=True)
        # pylint: disable=eval-used
        return eval(random.choice(question_choices))()
