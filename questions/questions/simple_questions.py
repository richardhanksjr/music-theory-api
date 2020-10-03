from .questions import Question


class SimpleIntervalIs(Question):

    def __init__(self):
        super().__init__()


    def _generate_answer(self):
        self._answer = "An interval that encompasses an octave or less"

    def _generate_answer_options(self):
        self._answer_options = ["A perfect interval", "A Major or minor interval",
                                "An interval that encompasses an octave or less",
                                "A consonant interval"]

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': 'What is a simple interval?',
                             'answer': 'an interval of one octave or less.'},)


    def _generate_question(self):
        self._question = "A SIMPLE INTERVAL is: "

    def _generate_question_type(self):
        self._question_type = "simple-interval-is"

    def _generate_question_params(self):
        self._question_params = {'question_type': self.question_type}

