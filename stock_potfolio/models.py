from django.db import models

from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.symbol

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    stocks = models.ManyToManyField(Stock, through='PortfolioStock')

    def __str__(self):
        return self.name

class PortfolioStock(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class StockStatus(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status
    
class Holding(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.stock} - Quantity: {self.quantity}, Value: {self.value}"

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

