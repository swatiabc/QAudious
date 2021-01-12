from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods

from . import models
from transcribe_audio.models import AudioDataModel

# Create your views here.
def question_page(request):
    return render(request,"question_2.html")


def qa_display_page(request):
    return render(request,"qa_display.html")


def qa_saved_page(request):
    return render(request,"qa_saved.html")

@require_http_methods(['GET', 'POST'])
def post_question(request):
    print("post question-------------------",request.method)
    if request.method == 'GET': 
        return render(request,"post_question.html")

    print("post question-------------------",request.method)
    uploaded_question = request.POST['uploaded_question']
    qa_data = models.QADataModel()
    qa_data.question = uploaded_question
    
    try:
        qa_data.transcript = AudioDataModel.objects.get(id=request.session['transcript'])
    except (KeyError, AudioDataModel.DoesNotExist):
        qa_data.transcript = None
    
    print("---------------------------------------------")
    print(qa_data.transcript.transcript)
    print("---------------------------------------------")
    qa_data.save()
    return HttpResponseRedirect("question_2.html")