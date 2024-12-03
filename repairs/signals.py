from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction, RevenueLog
from decimal import Decimal

@receiver(post_save, sender=Transaction)
def update_revenue_log(sender, instance, created, **kwargs):
    if created:
        print(instance.total_price)
        today_log, created = RevenueLog.objects.get_or_create(date=instance.transaction_date.date())
        
        if today_log.revenue is None:
            today_log.revenue = Decimal('0.00')

        today_log.revenue += instance.total_price 
        
        today_log.save()
