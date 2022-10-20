from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from main.models import Worker
from django.core.paginator import Paginator, EmptyPage, PageAnInteger
from .serializers import *

@api_view(['GET', 'POST'])
def workers_list(request):
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        workers = Worker.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(workers, 10)
        try:
            data = paginator.page(page)
        except PageAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializers = WorkersSerializer(data, context={'request': request}, many=True)

        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data, 'count': paginator.count, 'numpages': paginator.num_pages, 'nextlink': '/api/workes/?page=' + str(nextPage), 'prevlink': '/api/workes/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = WorkersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def workers_detail(request, pk):
    try:
        worker = Worker.objects.get(pk=pk)
    except Worker.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WorkersSerializer(worker, context={'request': request})
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = WorkersSerializer(worker, data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        worker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
