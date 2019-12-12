from django.shortcuts import render, get_object_or_404
from .models import Produk
def home(request):
    produks = Produk.objects.all()
    return render(request,"shop/home.html",{"produks": produks})
def detail(request,produk_id):
    products = get_object_or_404(Produk, pk=produk_id)

    return render(request, 'shop/detail.html',{'products':products})
def form(request):
    return render(request,"shop/form.html",{})
def submit(request):
    foto = request.POST['foto']
    nama = request.POST['nama']
    harga = request.POST['harga']

    new =Produk(foto = foto, nama = nama, harga = harga)
    new.save()

    produks = Produk.objects.all()
    return render(request, 'shop/home.html',{'produks': produks})