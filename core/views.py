from django.shortcuts import render
from rest_framework import generics
from .models import Member
from .serializers import MemberSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(('GET',))
def home_view(request):
    return Response({
        "GET": "/api/members",
        "GET(Single)": "/api/members/:id",
        "POST": "/api/members",
        "PUT": "/api/members/:id",
        "DELETE": "/api/members/:id",

        "request body": {
            'firstname': 'Ola',
            'lastname': 'Muktar',
            'stack': 'Python, Javascript, C#',

        }
    })


class MembersList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


@api_view(('GET','PUT', 'DELETE'))
def UpdateOrDeleteMemberView(request, pk):
    member = get_object_or_404(Member, id=pk)
    # member = Member.objects.get(id=pk)
    member_serializer = MemberSerializer(member, many=False)
    if request.method == "PUT":
        member_serializer = MemberSerializer(member, request.data)
        if member_serializer.is_valid():
            member_serializer.save()
            return Response(member_serializer.data)
        return Response(member_serializer.errors)

    elif request.method == "DELETE":
        member.delete()

    return Response(member_serializer.data)
    
    
        

