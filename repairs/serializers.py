from rest_framework import serializers
from .models import Component, Vehicle, Issue, Transaction, RevenueLog

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class RevenueLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueLog
        fields = '__all__'
