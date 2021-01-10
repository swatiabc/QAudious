from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods

from . import models
from . import tasks

# Create your views here.
def upload_page(request):
    return render(request,"upload.html")


@require_http_methods(['GET', 'POST'])
def local_page(request):
    """
    Main Home page
    """
    try:

        print("11111111111111")
        # GET method, return HTML page
        print("--------------",request.method)
        if request.method == 'GET':
            return render(request, 'local.html')


        print("--------------",request.method)
        # POST request, process the uploaded Audio file
        uploaded_file = request.FILES['uploaded_file']
        print("22222222222222222222222222")
        audio_data = models.AudioDataModel()
        print("3333333333333333333333")
        audio_data.uploaded_file=uploaded_file
        audio_data.save()

        # Begin processing
        tasks.process_uploaded_file.delay(audio_data.id)

        return HttpResponseRedirect('local.html')

    except Exception as e:

        audio_data.status = 'ERR'
        audio_data.error_occurred = True
        audio_data.error_message = str(e)
        audio_data.save()

        return HttpResponse(f'Error: {str(e)}')

def drive_page(request):
    return render(request,"drive.html")

def post_question(request):
    return render(request,"post_question.html")

@require_http_methods(['GET', 'POST'])
def home_view(request):
    """
    Main Home page
    """
    try:

        # GET method, return HTML page
        if request.method == 'GET':
            samples = models.AudioDataModel.objects.all()

            pending_jobs = models.AudioDataModel.objects.filter(status='PEN').count()
            show_timer = False
            if pending_jobs > 0:
                show_timer = True
            return render(request, 'home.html', {'samples': samples, 'show_timer': show_timer})

        # POST request, process the uploaded Audio file
        uploaded_file = request.FILES['uploaded_file']
        print("11111111111111111111")
        audio_data = models.AudioDataModel()
        print("2222222222222222222")
        audio_data.uploaded_file=uploaded_file
        audio_data.save()
        # audio_data = models.AudioDataModel.objects.create(uploaded_file=uploaded_file)

        # Begin processing
        tasks.process_uploaded_file(audio_data.id)

        return HttpResponseRedirect('/')

    except Exception as e:

        audio_data.status = 'ERR'
        audio_data.error_occurred = True
        audio_data.error_message = str(e)
        audio_data.save()

        return HttpResponse(f'Error: {str(e)}')