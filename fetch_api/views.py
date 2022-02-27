from rest_framework.generics import ListAPIView
from .serializers import PlaceHolderSerializer
from .models import PlaceHolder


class PlaceHolderListAPIView(ListAPIView):
    serializer_class = PlaceHolderSerializer

    def get_queryset(self):
        return PlaceHolder.objects.all()
