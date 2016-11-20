from rest_framework import serializers
from  .models import Mosques  , Timing

class mosqueserializer(serializers.ModelSerializer):
	class Meta:
		model = Mosques
		fields = '__all__'

class timingserializer(serializers.ModelSerializer):
	class Meta:
		model = Timing
		fields = '__all__'