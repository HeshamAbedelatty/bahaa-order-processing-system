# Generated by Django 4.2.16 on 2024-10-14 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_initial'),
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Not Paid', max_length=20),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
