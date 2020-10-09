import random
from .models import Question

"""
Questions are imported dynamically from the Question model.  The Question model
contains a module name and a class name.  First we import all question in the db
and then we add the class names to the list of question_choices.
"""


questions = Question.objects.all()
print("questions******************", questions)

# Dynamically import files
for question in questions:
    exec(f"from questions.questions.{question.module_name} import {question.class_name}")

question_choices = questions.values_list('class_name', flat=True)



class QuestionGenerator:

    @staticmethod
    def question_factory():
        """
        Used to get a random question. Returns a random question instance
        from question_choices.
        """
        return eval(random.choice(question_choices))()
