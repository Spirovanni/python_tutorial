# Generated by Django 2.2.7 on 2019-11-12 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20191111_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(choices=[('FRESHMAN', 'Freshman'), ('SOPHOMORE', 'Sophomore'), ('JUNIOR', 'Junior'), ('SENIOR', 'Senior')], max_length=36, null=True),
        ),
    ]
