from rest_framework import status, views
from rest_framework.response import Response

from psicoApp.models.psychologist import Psychologist
from psicoApp.serializers.psychologistSerializer import PsychologistSerializer

class PsychologistsDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        psychologists = Psychologist.objects.all()
        serializer = PsychologistSerializer(psychologists)
        return Response(serializer.data)