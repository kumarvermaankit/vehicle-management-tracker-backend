from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComponentViewSet, VehicleViewSet, IssueViewSet, TransactionViewSet, RevenueLogViewSet, MonthlyRevenueView

router = DefaultRouter()
router.register(r'components', ComponentViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'issues', IssueViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'revenue_logs', RevenueLogViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/revenue/', MonthlyRevenueView.as_view(), name='monthly-revenue'),
]
