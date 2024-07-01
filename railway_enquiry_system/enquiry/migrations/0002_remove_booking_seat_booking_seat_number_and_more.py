# Generated by Django 5.0.6 on 2024-06-20 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='seat',
        ),
        migrations.AddField(
            model_name='booking',
            name='seat_number',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='train',
            name='available_seats',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AddField(
            model_name='train',
            name='total_seats',
            field=models.PositiveIntegerField(default=50),
        ),
    ]
