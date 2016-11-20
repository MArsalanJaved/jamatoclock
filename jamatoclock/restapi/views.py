from .models import Mosques , Timing
from .serializers import mosqueserializer ,timingserializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def mosque_list(request , format = None):
	if request.method == 'GET':
		mosque = Mosques.objects.all()
		serializer = mosqueserializer(mosque, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = mosqueserializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def mosques_detail(request, pk , format = None):
	try:
		mosque = Mosques.objects.get(gmap_id = pk)
	except Mosques.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = mosqueserializer(mosque)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = SnippetSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		mosque.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE'])
def timings_detail(request, pk , format = None):
	try:
		mosque = Mosques.objects.get(gmap_id = pk)
		time = Timing.objects.get(mosque_id = mosque.id)
	except Timing.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = timingserializer(time)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = timingserializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		mosque.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)