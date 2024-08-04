from paycomuz.views import MerchantAPIView
from paycomuz import Paycom
from django.urls import path
from order.models import Order

class CheckOrder(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        order = Order.objects.filter(id=account['order_id'], is_fineshed=False).first()
        if not order:
             return self.ORDER_NOT_FOND
        if order.total * 100 != amount:
             return self.INVALID_AMOUNT
        
        return self.ORDER_FOUND
        
    def successfully_payment(self, account, transaction, *args, **kwargs):
        order = Order.objects.filter(id=transaction.order_key).filter()
        if not order:
            return self.ORDER_NOT_FOND
        order.is_finished = True
        order.save()


    def cancel_payment(self, account, transaction, *args, **kwargs):
        print(account)
      

class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder
