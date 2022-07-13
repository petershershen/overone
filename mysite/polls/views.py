from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

class  IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    
# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by("pub_date")[:5]
#     # template = loader.get_template("polls/index.html")
#     context = {"latest_question_List": latest_question_list}
#     # output = ",".join([q.question_text for q in latest_question_list])
#     return render(request, "polls/index.html", context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    class ResultsView(generic.DetailView):
        model =Question
        template_name = 'polls/results.html'

# def detail(request, question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     # return HttpResponse("You're looking at question %s." % question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render((request, "polls/result.html", {"question": question}))

    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render((request,"polls/detail.html",
                       {"question": question, "error_message": "U didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirest(reverse("polls: results", args=(question_id,)))



    # return HttpResponse("You're voting on question %s." % question_id)
