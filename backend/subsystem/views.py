from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.
class SubsystemViewSet(viewsets.ModelViewSet):
    queryset = Subsystem.objects.all()
    serializer_class = SubsystemSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

class ClassFetchAPIView(viewsets.ModelViewSet):
    serializer_class = ClassRoomSerializer
    def get_queryset(self):
        school = self.request.query_params.get('school', None)
        if school is not None:
            return ClassRoom.objects.filter(school=school)
        else:
            return ClassRoom.objects.all()

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class SubDivisionViewSet(viewsets.ModelViewSet):
    queryset = SubDivision.objects.all()
    serializer_class = SubDivisionSerializer

class LocalityViewSet(viewsets.ModelViewSet):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer
