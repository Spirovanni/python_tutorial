from django.db import models


# Create your models here.
class Book(models.Model):
    # BOOKS = [
    #     ('FRESHMAN', 'Freshman'),
    #     ('SOPHOMORE', 'Sophomore'),
    #     ('JUNIOR', 'Junior'),
    #     ('SENIOR', 'Senior'),
    # ]
    title = models.CharField(
        max_length=36,
        null=True,
        # unique=True,
        # choices=BOOKS
    )
    description = models.TextField(max_length=256, blank=True, null=True, default=None)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=3)
    is_published = models.BooleanField(default=False)

    # cover = models.ImageField(upload_to='covers/', blank=True)
