from rest_framework import viewsets
from .models import Component, Vehicle, Issue, Transaction, RevenueLog
from .serializers import ComponentSerializer, VehicleSerializer, IssueSerializer, TransactionSerializer, RevenueLogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from datetime import datetime

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class RevenueLogViewSet(viewsets.ModelViewSet):
    queryset = RevenueLog.objects.all()
    serializer_class = RevenueLogSerializer

class MonthlyRevenueView(APIView):
    def get(self, request):
        print(request)
        year = request.query_params.get('year', datetime.now().year)
        revenue_data = RevenueLog.objects.filter(date__year=year).values('date__month').annotate(total_revenue=Sum('revenue'))
        return Response(revenue_data)