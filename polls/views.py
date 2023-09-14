from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    context_object_name = 'question'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'
    context_object_name = 'question'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_one = question.choice_set.get(pk=request.POST['choice'])
    except (Choice.DoesNotExist, KeyError):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'please choose any one!',
        })
    else:
        selected_one.votes += 1
        selected_one.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))