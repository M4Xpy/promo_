from time import time

########################################################################################################################

text = """
We’ll discuss what you could put in that polls/detail.html template a bit later, but if you’d like to quickly get the above example working, a file containing just:

polls/templates/polls/detail.html¶
{{ question }}
will get you started for now.

A shortcut: get_object_or_404()¶
It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. Django provides a shortcut. Here’s the detail() view, rewritten:

polls/views.py¶
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager. It raises Http404 if the object doesn’t exist.

Philosophy

Why do we use a helper function get_object_or_404() instead of automatically catching the ObjectDoesNotExist exceptions at a higher level, or having the model API raise Http404 instead of ObjectDoesNotExist?

Because that would couple the model layer to the view layer. One of the foremost design goals of Django is to maintain loose coupling. Some controlled coupling is introduced in the django.shortcuts module.

There’s also a get_list_or_404() function, which works just as get_object_or_404() – except using filter() instead of get(). It raises Http404 if the list is empty.

Use the template system¶
Back to the detail() view for our poll application. Given the context variable question, here’s what the polls/detail.html template might look like:

polls/templates/polls/detail.html¶
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
The template system uses dot-lookup syntax to access variable attributes. In the example of {{ question.question_text }}, first Django does a dictionary lookup on the object question. Failing that, it tries an attribute lookup – which works, in this case. If attribute lookup had failed, it would’ve tried a list-index lookup.

Method-calling happens in the {% for %} loop: question.choice_set.all is interpreted as the Python code question.choice_set.all(), which returns an iterable of Choice objects and is suitable for use in the {% for %} tag.

See the template guide for more about templates.
""" * 99

########################################################################################################################
time_1 = time()
########################################################################################################################

def pig_it(text):
    """ 501ms-662ms   TEST 503ms-699ms  ATTEMPT"""
    return ' '.join(word[1:] + word[0] + 'ay'
                    if word.isalpha()
                    else word
                    for word in text.split())
pig_it(text)
########################################################################################################################
time_2 = time()
ttt = time_2 - time_1
time_1 = time()
########################################################################################################################

def pig_it(text):
    """ 483ms-527ms  TEST 476ms-517ms  ATTEMPT"""
    return ' '.join(f'{word[1:]}{word[0]}ay'
                    if word.isalpha()
                    else word
                    for word in text.split())
pig_it(text)
########################################################################################################################
time_2 = time()
print(f'TIME : {ttt}')
print(f'TIME : {time_2 - time_1}')
print(f'RATIO : {ttt / (time_2 - time_1)}')
