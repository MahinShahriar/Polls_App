from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Question, Choice
from .utils import get_plot

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    choices = question.choice_set.all()
    # Extract x and y values from choices
    x = [x.choice_text for x in choices]
    y = [y.votes for y in choices]
    chart = get_plot(x,y)
    context = {
        "chart" : chart,
        "question" : question,
    }
    return render(request, "polls/results.html", context)

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question" : question,
                "error_message" : "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results",args=(question_id,)))

