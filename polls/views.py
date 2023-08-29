from django.db import models
from django.utils import timezone
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choix
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView


# Create your views here.
# IndexView hérite la classe ListView qui est une vue générique
#
def logins(request):
    return render(request, "polls/login.html")

class IndexView(ListView):
    # model=Question
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"


    def get_queryset(self):
        # retourne les six dernières questions publié
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:10]
        


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list,}
#     return render(request, "polls/index.html", context)

class DetailView(DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name="question"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

    # try:
    #     # question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "polls/detail.html", {"question": question})
class ResultsView(DetailView):
    model = Question
    template_name = "polls/results.html"

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question":question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selectionner_choix = question.choix_set.get(pk=request.POST["choix"])
    except (KeyError, Choix.DoesNotExist):
        # redirection de question de vote
        context = {"question":question, "error_message":"Vous n'avez pas selectonner un choix.",}
        return render(request, "polls/detail.html", context)
    else:
        selectionner_choix.votes += 1
        selectionner_choix.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

