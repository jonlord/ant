from django.db import models


class Order(models.Model):
    number = models.CharField(max_length=200)
    date = models.DateField()
    client = models.CharField(max_length=255)
    marketplace = models.CharField(max_length=255)
    eurozone = models.IntegerField()
    status = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    processed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number


class Row(models.Model):
    product_reference = models.CharField(max_length=255)
    color_reference = models.CharField(max_length=255)
    size_position = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=4)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    warehouse = models.CharField(max_length=255, default=0)

    #def __str__(self):
    #    return self.product_reference + ' ' + self.color_reference + ' ' + self.size_position
