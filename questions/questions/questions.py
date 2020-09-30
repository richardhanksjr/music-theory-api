from abc import ABC


class Question(ABC):

    def __init__(self):
        self._generate_question()
        self._generate_answer()
        self._generate_answer_options()
        self._generate_help_steps_array()
        self._generate_key()
        self._generate_response()
        self._add_to_cache()

    def _generate_response(self):
        raise NotImplementedError

    def _add_to_cache(self):
        raise NotImplementedError

    def _generate_question(self):
        raise NotImplementedError

    def _generate_answer(self):
        raise NotImplementedError

    def _generate_answer_options(self):
        raise NotImplementedError

    def _generate_help_steps_array(self):
        raise NotImplementedError

    def _generate_key(self):
        raise NotImplementedError

    @property
    def question(self):
        raise NotImplementedError

    @property
    def answer_options(self):
        raise NotImplementedError

    @property
    def answer(self):
        raise NotImplementedError

    @property
    def question_type(self):
        raise NotImplementedError

    @property
    def question_params(self):
        raise NotImplementedError

    @property
    def help_steps(self):
        raise NotImplementedError
