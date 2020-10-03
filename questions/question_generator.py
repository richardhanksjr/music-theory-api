import random
from .questions.simple_questions import SimpleIntervalIs
from .questions.major_scale_questions import SimpleScaleDegreeMajor
question_choices = [
    SimpleIntervalIs, SimpleScaleDegreeMajor
]


class QuestionGenerator:

    @staticmethod
    def question_factory():
        """
        Used to get a random question. Returns a random question instance
        from question_choices.
        """
        return random.choice(question_choices)()
