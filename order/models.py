from django.db import models

# Create your models here.


class Order(models.Model):
    title = models.CharField(max_length=190)
    total = models.CharField(max_length=50)
    is_finished = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f"{self.id} {self.total}"
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'