from rest_framework import generics
from .models import Steps
from .serializers import StepSerializer

# Create your views here.
class ListCreateSteps(generics.ListCreateAPIView):
    """
        view to list all steps entries
    """
    queryset = Steps.objects.all()
    serializer_class = StepSerializer