from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods

from . import models

# Create your views here.
def question_page(request):
    return render(request,"question_2.html")


def qa_display_page(request):
    return render(request,"qa_display.html")


def qa_saved_page(request):
    return render(request,"qa_saved.html")

@require_http_methods(['GET', 'POST'])
def post_question(request):
    if request.method == 'GET':
        return render(request,"post_question.html")

    uploaded_question = request.FILES['uploaded_question']
    qa_data = models.QADataModel()
    qa_data.question = uploaded_question
    qa_data.transcript = 