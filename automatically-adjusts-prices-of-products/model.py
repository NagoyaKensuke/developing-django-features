from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        if self.stock < 10:
            self.current_price = self.base_price * 1.2  # 在庫が少ない場合、価格を20%上げる
        elif self.stock > 50:
            self.current_price = self.base_price * 0.9  # 在庫が多い場合、価格を10%下げる
        else:
            self.current_price = self.base_price  # 在庫が適切な場合、基本価格を維持
        super(Product, self).save(*args, **kwargs)
