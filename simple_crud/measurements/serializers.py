from rest_framework import serializers

from measurements.models import Measurement, Project


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'project', 'temperature', 'value', 'created_at']


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description']


class ProjectDetailSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'measurements']