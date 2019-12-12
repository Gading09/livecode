from django.db import models

# Create your models here.
class Produk(models.Model):
    foto = models.CharField(max_length = 255, default = "")
    nama = models.CharField(max_length = 255, default = "")
    harga = models.CharField(max_length = 255, default = "")

    def __str__(self):
        return self.nama

class Info(models.Model):
    produk_key = models.ForeignKey(Produk, on_delete=models.CASCADE)
    deskripsi = models.TextField(default = "")

    def __str__(self):
        return self.choice_text