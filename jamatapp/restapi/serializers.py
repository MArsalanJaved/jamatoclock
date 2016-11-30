from rest_framework import serializers
from  .models import Mosques  , Timing

class mosqueserializer(serializers.ModelSerializer):
	gmap_id = serializers.CharField(max_length= 50 )
	mosque_name  = serializers.CharField(max_length = 100)
	long_location  = serializers.FloatField()
	lat_location   = serializers.FloatField()
	class Meta:
		model = Mosques
		fields = '__all__'

class timingserializer(serializers.ModelSerializer):
	
	class Meta:
		model = Timing
		fields = '__all__'