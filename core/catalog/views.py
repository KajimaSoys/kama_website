from rest_framework import generics, filters
from django_filters import rest_framework as django_filters
from .models import Sofa
from .serializers import (
    SofaListSerializer,
    SofaDetailSerializer
)


# Фильтры для Sofa
class SofaFilter(django_filters.FilterSet):
    sofa_type = django_filters.CharFilter(field_name='sofa_type')

    class Meta:
        model = Sofa
        fields = ['sofa_type']


# Представление для списка диванов
class SofaListView(generics.ListAPIView):
    queryset = Sofa.objects.all().prefetch_related('images')
    serializer_class = SofaListSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = SofaFilter


# Представление для детального описания дивана
class SofaDetailView(generics.RetrieveAPIView):
    queryset = Sofa.objects.all().prefetch_related('images', 'reviews', 'other_variants')
    serializer_class = SofaDetailSerializer
