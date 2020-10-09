# import random
from .models import Question, Tag
# from django.db.utils import ProgrammingError
#
# """
# Questions are imported dynamically from the Question model.  The Question model
# contains a module name and a class name.  First we import all question in the db
# and then we add the class names to the list of question_choices.
# """
#
#

# try:
#     print("questions******************", questions)
# except ProgrammingError as e:
#     print("top block")
#     print("e")
#
# # Dynamically import files
# for question in questions:
#     try:
#         exec(f"from questions.questions.{question.module_name} import {question.class_name}")
#     except ProgrammingError as e:
#         print("error is: ", e)
#
#
# question_choices = questions.values_list('class_name', flat=True)
#
#
#
class QuestionGenerator:
    print("tags", Tag.objects.all())
    questions = Question.objects.all()
    print("questions*****", questions)
#
#     @staticmethod
#     def question_factory():
#         """
#         Used to get a random question. Returns a random question instance
#         from question_choices.
#         """
#         return eval(random.choice(question_choices))()
