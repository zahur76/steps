from rest_framework import generics
from .models import Steps
from .serializers import StepSerializer
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view


# Create your views here.
@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(
                name="start_date", description="start_date", type=str, required=False
            ),
            OpenApiParameter(
                name="end_date", description="end_date", type=str, required=False
            ),
            OpenApiParameter(
                name="step_above",
                description="steps Above",
                type=int,
                required=False,
            ),
            OpenApiParameter(
                name="step_below",
                description="Steps Below",
                type=int,
                required=False,
            ),
        ]
    )
)
class ListCreateSteps(generics.ListCreateAPIView):
    """
        view to List and Create all steps entries
    """
    queryset = Steps.objects.all()
    serializer_class = StepSerializer

    # def get_queryset(self):

        