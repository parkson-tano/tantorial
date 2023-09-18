from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
# Create your views here.
class SubsystemViewSet(viewsets.ModelViewSet):
    queryset = Subsystem.objects.all()
    serializer_class = SubsystemSerializer
    permission_classes = [permissions.AllowAny]

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

    def get_queryset(self):
        queryset = self.queryset
        school = self.request.query_params.get('school', None)
        if school is not None:
            return queryset.filter(school=school)

        return queryset

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = self.queryset
        school = self.request.query_params.get('school', None)
        if school is not None:
            return queryset.filter(school=school)

        return queryset

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get_queryset(self):
        queryset = self.queryset
        country = self.request.query_params.get('country', None)
        if country is not None:
            return queryset.filter(country=country)

        return queryset

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

    def get_queryset(self):
        queryset = self.queryset
        region = self.request.query_params.get('region', None)
        if region is not None:
            return queryset.filter(region=region)

        return queryset

class SubDivisionViewSet(viewsets.ModelViewSet):
    queryset = SubDivision.objects.all()
    serializer_class = SubDivisionSerializer

    def get_queryset(self):
        queryset = self.queryset
        division = self.request.query_params.get('division', None)
        if division is not None:
            return queryset.filter(division=division)

        return queryset

class LocalityViewSet(viewsets.ModelViewSet):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer

    def get_queryset(self):
        queryset = self.queryset
        subdivision = self.request.query_params.get('subdivision', None)
        if subdivision is not None:
            return queryset.filter(subdivision=subdivision)

        return queryset