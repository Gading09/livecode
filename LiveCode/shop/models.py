from django.db import models

# Create your models here.
class Produk(models.Model):
    foto = models.CharField(max_length = 255, default = "")
    nama = models.CharField(max_length = 255, default = "")
    harga = models.CharField(max_length = 255, default = "")

    def __str__(self):
        return self.nama