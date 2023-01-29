from django.shortcuts import render
from rest_framework import generics
from .models import Member
from .serializers import MemberSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# Create your views here.


class MembersList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

@api_view(('GET',))
def MemberView(request, pk):
    member = Member.objects.get(id=pk)
    member_serializer = MemberSerializer(member, many=False)
    return Response(member_serializer.data)


@api_view(('GET','PUT', 'DELETE'))
def UpdateOrDeleteMemberView(request, pk):
    member = Member.objects.get(id=pk)
    member_serializer = MemberSerializer(member, request.data)
    if request.method == "PUT":
        if member_serializer.is_valid():
            member_serializer.save()
            return Response(member_serializer.data)
        return Response(member_serializer.errors)

    elif request.method == "DELETE":
        if member_serializer.is_valid():
            member_serializer.delete()
            return Response(member_serializer.data)
        return Response(member_serializer.errors)

    return Response()
    
    
        

