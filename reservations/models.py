from django.db import models

# Create your models here.

class Yatch_Main(models.Model):
    id = models.AutoField(primary_key=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yenilenme Tarihi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")

    class Meta:
        verbose_name = "Yatch Master"
        verbose_name_plural = "Yatch Master"

    def __str__(self):
        return str(self.created_at)

class Yatch_Reservation(models.Model):
    id_related = models.ForeignKey(Yatch_Main, on_delete=models.CASCADE, verbose_name="id",help_text='id')
    reservation_date = models.DateField(verbose_name="Reservation Date")
    pax = models.FloatField(verbose_name="Pax", default=0, )
    tour_code = models.CharField(max_length=20, verbose_name='Tour Code', null=True, blank=True)
    customer = models.CharField(max_length=250, verbose_name='Customer', null=True, blank=True)
    nofplace = models.CharField(max_length=50, verbose_name='From to', null=True, blank=True)
    tour_detail = models.TextField(verbose_name='Tour Details', null=True, blank=True)
    yatch_name = models.CharField(max_length=250, verbose_name='Yatch Name', null=True, blank=True)
    guide = models.CharField(max_length=50, verbose_name='Guide', null=True, blank=True)
    operation = models.CharField(max_length=50, verbose_name='Operation', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yenilenme Tarihi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")


    class Meta:
        verbose_name = "Yatch Reservation"
        verbose_name_plural = "Yatch Reservation"

    def __str__(self):
        return str(self.id_related)




