from django.db import models

# Create your models here.

class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return "{}. {}" .format(self.nama,self.ket)

class Barang(models.Model):
    kodebrg=models.CharField(max_length=8, default="BRG")
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "{}. {}. {}. {}. {}" .format(self.kodebrg,self.nama,self.stok,self.harga,self.link_gbr)

class Transaksi(models.Model):
    kodetrans=models.CharField(max_length=10)
    tgltrans=models.DateTimeField(auto_now_add=True)
    total=models.BigIntegerField()

    def __str__(self):
        return self.kodetrans

class Detailtrans(models.Model):
    kodetrans=models.CharField(max_length=10)
    kodebrg=models.CharField(max_length=8)
    qty=models.IntegerField()
    subtotal=models.BigIntegerField()
    
    def __str__(self):
        return "{}. {}. {}. {}. {}" .format(self.kodetrans,self.kodebrg)

class Member(models.Model):
    idmember=models.CharField(max_length=10)
    nama=models.CharField(max_length=25)
    alamat=models.CharField(max_length=30)

    def __str__(self):
        return "{}. {}. {}" .format(self.idmember,self.nama,self.alamat)