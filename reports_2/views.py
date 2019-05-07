from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from reports_2.models import ApplyLeave
from reports_2.serializer import applyleaveserializer
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime,date
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.http import JsonResponse,HttpResponse
from worksnaps_report import settings
from django.core.mail import get_connection, EmailMultiAlternatives, send_mail


class ApplyLeaveView(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)		
	serializer_class = applyleaveserializer
	
	def post(self,request):
	    serializer = applyleaveserializer(data = request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data, status=status.HTTP_201_CREATED)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class leave_details(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = applyleaveserializer

	def get_queryset(self):
		user = self.request.user
		local_time = datetime.now()
		return ApplyLeave.objects.filter(leave_start_date__gte=local_time,leave_status=False,user=user)

	def get(self,request,*args,**kwargs):	
		serializer = applyleaveserializer(self.get_queryset(), many=True)
		data = serializer.data[:]
		return Response(data, status=status.HTTP_200_OK)

	
	def get_object(self, id):
		try:
			return ApplyLeave.objects.get(id=id)
		except ApplyLeave.DoesNotExist:
			raise Http404

	def put(self, request):
		user = request.user
		if user.is_superuser:
			instance_id = request.data.get('id')
			user = self.get_object(instance_id)
			serializer = applyleaveserializer(instance=user, data=request.data, partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

