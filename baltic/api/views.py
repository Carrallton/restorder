from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from main.models import UserProfile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db import models

class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.order_by("pk")
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        qs = qs.filter(user=self.request.user)

        search = self.request.query_params.get("search", None)
        if search:
            qs = qs.filter(
                models.Q(name__icontains=search)
                | models.Q(phone__icontains=search)
                | models.Q(email__icontains=search)
            )

        return qs


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

#@api_view(['GET', 'POST'])
#def workers_list(request):
#    if request.method == 'GET':
#        data = []
#        previousPage = 1
#        workers = Worker.objects.all()
#        page = request.GET.get('page', 1)
#        paginator = Paginator(workers, 10)
#        try:
#            data = paginator.page(page)
#        except PageNotAnInteger:
#            data = paginator.page(1)
#
#
#        serializers = WorkersSerializer(data, context={'request': request}, many=True)
#
#        if data.has_next():
#            nextPage = data.next_page_number()
#        if data.has_previous():
#            previousPage = data.previous_page_number()
#
#        return Response({'data': serializer.data, 'count': paginator.count, 'numpages': paginator.num_pages, 'nextlink': '/api/workes/?page=' + str(nextPage), 'prevlink': '/api/workes/?page=' + str(previousPage)})

#    elif request.method == 'POST':
#        serializer = WorkersSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['GET', 'PUT', 'DELETE'])
#def workers_detail(request, pk):
#    try:
#        worker = Worker.objects.get(pk=pk)
#    except Worker.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)

#    if request.method == 'GET':
#        serializer = WorkersSerializer(worker, context={'request': request})
#        return Response(serializer.data)

#    if request.method == 'PUT':
#        serializer = WorkersSerializer(worker, data=request.data, context={'request':request})
#        if serializer.is_valid():
#            serializer.save()
#            return(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    if request.method == 'DELETE':
#        worker.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
