from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.conf import settings
from .models import Choice, Question


class IndexView(generic.ListView):
    """Index view"""
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_context_data(self, **kwargs):
        """Subclass so that we can pass in extra stuff."""
        context = super(IndexView, self).get_context_data(**kwargs)
        context['version'] = settings.VERSION
        return context

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()
                                       ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        """Subclass so that we can pass in extra stuff."""
        context = super(DetailView, self).get_context_data(**kwargs)
        context['version'] = settings.VERSION
        return context

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_context_data(self, **kwargs):
        """Subclass so that we can pass in extra stuff."""
        context = super(ResultsView, self).get_context_data(**kwargs)
        context['version'] = settings.VERSION
        return context


def vote(request, question_id):
    """Vote view"""
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
            'version': settings.VERSION,
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
