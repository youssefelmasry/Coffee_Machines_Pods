from django.db import models

class CommonInfo(models.Model):
    """
    An abstract common info model class for Coffee machines and Coffee pods models
    Which shares the same attributes, SKU code & product type
    """
    code = models.CharField(max_length=7)
    product_type = models.CharField(max_length=20)

    class Meta:
        abstract=True

class CoffeeMachines(CommonInfo):
    water_line_compatible = models.BooleanField(default=False)
    model_type = models.CharField(max_length=15)

    def __str__(self):
        return self.code

class CoffeePods(CommonInfo):
    coffee_flavor = models.CharField(max_length=15)
    pack_size = models.CharField(max_length=10)

    def __str__(self):
        return self.code
    