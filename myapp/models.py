from django.db import models
from django.contrib.auth.models import User
from myapp.functions.fileValidation import validate_file_extension
# Create your models here.
class Venue(models.Model):
    vid=models.AutoField(primary_key=True)
    vname=models.CharField(max_length=255, verbose_name='Venue Name')
    vdescriptions=models.TextField(verbose_name='Venue Descripton')
    vtype=models.CharField(max_length=50, verbose_name='Venue Type')
    vaddress=models.CharField(max_length=255, verbose_name='Venue Address')
    vcharges=models.CharField(max_length=15, verbose_name='Venue Charges')
    file = models.FileField(upload_to="uploads/", validators=[validate_file_extension], verbose_name='Venue Image')
    def __str__(self) -> str:
        return self.vname

class Book(models.Model):
    bid=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_by', verbose_name='Book By')
    venue=models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='venue', verbose_name='Venue Name')
    description=models.CharField(max_length=255, verbose_name="Event Descriptions")
    bookdate=models.DateTimeField(auto_now_add=True, blank=False, verbose_name='Book Date')
    from_date=models.DateField(verbose_name='booking date',null=True, blank=True)
    end_date=models.DateField(verbose_name='end date',null=True, blank=True)
    charges=models.CharField(max_length=25)
    status=models.BooleanField(default=True)