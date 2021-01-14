from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods

from . import model_answer
from . import models
from transcribe_audio.models import AudioDataModel

# Create your views here.
def question_page(request):
    print("-------------question_2-----------------------")
    return render(request,"question_2.html")


def qa_display_page(request):
    return render(request,"qa_display.html")


@require_http_methods(['GET', 'POST'])
def qa_delete_confirm_page(request):
    if 'qa_data' not in request.session:
        return HttpResponseRedirect("post_question.html")
    
    if request.method == 'GET': 
        return render(request,"qa_delete_confirm.html")

    try:
        qa_data = models.QADataModel.objects.get(id=request.session['qa_data'])
    except (KeyError, models.QADataModel.DoesNotExist):
        qa_data = None    
    
    models.QADataModel.objects.filter(id=qa_data.id).delete()
    del request.session["qa_data"]
    
    return render(request, "qa_deleted.html")


def qa_deleted_page(request):
    if 'qa_data' not in request.session:
        return HttpResponseRedirect("post_question.html")

    return render(request,"qa_deleted.html")

def qa_saved_page(request):
    return render(request,"qa_saved.html")


@require_http_methods(['GET', 'POST'])
def post_question(request):

    if 'transcript' not in request.session:
        return HttpResponseRedirect("upload.html")

    abc = AudioDataModel.objects.get(id=request.session['transcript'])  
    print("---------------------------------session",abc.id)  
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
    qa_data.answer = model_answer.get_answer()
    qa_data.save()
    request.session["qa_data"]=qa_data.id
    return HttpResponseRedirect("qa_display.html")