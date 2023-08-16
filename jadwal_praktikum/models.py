from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Sesi(models.Model):
    
    class Hari(models.TextChoices):
        SENIN = "SN", _("Senin")
        SELASA = "SL", _("Selsasa")
        RABU = "RB", _("Rabu")
        KAMIS = "KM", _("Kamis")
        JUMAT = "JM", _("Jumat")
        SABTU = "SB", _("Sabtu")
    
    hari = models.CharField(
        max_length=2,
        choices=Hari.choices,
        default=Hari.SENIN
    )
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    kode = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.hari

    class Meta:
        verbose_name_plural = "Sesi"

class Ruang(models.Model):
    nomor = models.CharField(max_length=4)
    lantai = models.CharField(max_length=1)

    def __str__(self) -> str:
        return self.nomor

    class Meta:
        verbose_name_plural = "Ruang"

class Matkul(models.Model):
    nama = models.CharField(max_length=15)
    dosen = models.CharField(max_length=50)
    kontak = models.CharField(max_length=13)

    def __str__(self) -> str:
        return self.nama

    class Meta:
        verbose_name_plural = "Matkul"

class Jadwal(models.Model):
    sesi = models.ForeignKey(Sesi, on_delete=models.SET_NULL, null=True)
    matkul = models.ForeignKey(Matkul, on_delete=models.SET_NULL, null=True)
    ruang = models.ForeignKey(Ruang, on_delete=models.SET_NULL, null=True)
    kelas = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self) -> str:
        return self.kelas

    class Meta:
        verbose_name_plural = "Jadwal"

class Asprak(models.Model):
    kode = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.kode

    class Meta:
        verbose_name_plural = "Asprak"

class Praktikan(models.Model):
    kelas = models.CharField(max_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.kelas

    class Meta:
        verbose_name_plural = "Praktikan"

class PlotPraktikan(models.Model):
    jadwal = models.ForeignKey(Jadwal, on_delete=models.CASCADE)
    asprak = models.ForeignKey(Asprak, on_delete=models.CASCADE)
    praktikan = models.ForeignKey(Praktikan, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Plot Praktikan"

class PlotMatkul(models.Model):
    asprak = models.ForeignKey(Asprak, on_delete=models.CASCADE)
    matkul = models.ForeignKey(Matkul, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Plot Matkul"


