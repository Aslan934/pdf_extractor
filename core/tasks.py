from celery import shared_task
from pdfextract.celery import app
from .models import File
import PyPDF2
import celery
from django.contrib.auth.models import User


@app.task(bind=True)
@shared_task
def extractor(file_id, user_id):
    user = User.objects.get(id=user_id)
    fileModel = File.objects.get(id=file_id, owner=user)
    reader = PyPDF2.PdfFileReader(fileModel.filePdf)
    content = ''
    for page in range(reader.getNumPages()):
        content += reader.getPage(page).extractText()
    fileModel.content = content
    fileModel.task_id = extractor.request.id
    fileModel.save()
