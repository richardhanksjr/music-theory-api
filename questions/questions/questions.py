from abc import ABC, abstractmethod
import uuid
import inspect
from django.core.cache import cache
from questions.models import Question as QuestionModel


class Question(ABC):

    def __init__(self):
        self._generate_question()
        self._generate_answer()
        self._generate_answer_options()
        self._generate_help_steps_array()
        self._get_tags()
        self._generate_key()
        self._generate_weight()
        self._generate_question_type()
        self._generate_question_params()
        self._generate_response()
        self._add_to_cache()



    def _generate_response(self):
        self._response = {
            'question': self.question,
            'answer_options': self.answer_options,
            'question_params': self.question_params,
            'key': self.key,
            'answer': self.answer
        }

    def _add_to_cache(self):
        key = self.response['key']
        data = {**self.response, **{'answer': self.answer}}
        cache.set(key, data)

    def _generate_key(self):
        self._key = str(uuid.uuid4())

    def _generate_weight(self):
        # The weight of a question is based on the length of keyword arguments
        # passed to the constructor.  This is a proxy for the complexity of the question.
        self._weight= len(inspect.getfullargspec(self.__init__).args)


    def _get_tags(self):
        class_name = self.__class__.__name__
        self._tags = QuestionModel.objects.get(class_name=class_name).tag_set.all().values_list('name', flat=True)

    @abstractmethod
    def _generate_question(self):
        pass

    @abstractmethod
    def _generate_answer(self):
        pass

    @abstractmethod
    def _generate_answer_options(self):
        pass

    @abstractmethod
    def _generate_help_steps_array(self):
        pass

    @abstractmethod
    def _generate_question_type(self):
        pass

    @abstractmethod
    def _generate_question_params(self):
        pass

    @property
    def answer_options(self):
        return self._answer_options

    @property
    def answer(self):
        return self._answer

    @property
    def question_type(self):
        return self._question_type

    @property
    def question_params(self):
        return self._question_params

    @property
    def help_steps(self):
        return self._help_steps

    @property
    def response(self):
        return self._response

    @property
    def key(self):
        return self._key

    @property
    def question(self):
        return self._question

    @property
    def tags(self):
        return self._tags

    @property
    def weight(self):
        return self._weight
