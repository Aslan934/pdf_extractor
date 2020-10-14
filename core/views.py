from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from celery.result import AsyncResult
from .models import File
from .tasks import extractor


class CreateView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    def post(self, request, filename=None, *args, **kwargs):
        fileModel = File()
        fileModel.filePdf = request.FILES['file']
        fileModel.owner = request.user
        fileModel.save()
        extractor.delay(fileModel.id, fileModel.owner.id)

        return Response(fileModel.id)


class CheckStatus(APIView):
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'id'

    def get_queryset(self, request):
        id = self.kwargs.get(self.lookup_url_kwarg)
        self.data = File.objects.get(id=id, owner=request.user)
        return self.data

    def get(self, request, id=None):
        result = AsyncResult(self.get_queryset(request).task_id)
        if result.state == 'SUCCESS':
            return Response(self.get_queryset(request).content)
        return Response(result.state)
