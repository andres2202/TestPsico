from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from psicoApp.models.psychologist import Psychologist
from psicoApp.serializers.psychologistSerializer import PsychologistSerializer

class PsychoDetailView(generics.RetrieveAPIView):
    queryset = Psychologist.objects.all()
    serializer_class = PsychologistSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail': 'Unathorized Request'}
            return Response(stringResponse, status=HTTP_401_UNAUTHORIZED)

        return super().get(request, *args , **kwargs)