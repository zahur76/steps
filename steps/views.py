from rest_framework import generics
from .models import Steps
from .serializers import StepSerializer
from django_filters import rest_framework as filters


# Create your views here.
class StepsFilter(filters.FilterSet):
    min_steps = filters.NumberFilter(field_name="steps", lookup_expr='gte')
    max_steps = filters.NumberFilter(field_name="steps", lookup_expr='lte')
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = Steps
        fields = ['steps'] # exact match without definition above


class ListCreateSteps(generics.ListCreateAPIView):
    """
        view to List and Create all steps entries
    """
    queryset = Steps.objects.all()
    serializer_class = StepSerializer

    # filter classes
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StepsFilter
        