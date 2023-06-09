# Generated by Django 4.1.5 on 2023-05-10 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_image', models.ImageField(upload_to='qr_codes/')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapps.patient')),
            ],
        ),
    ]
