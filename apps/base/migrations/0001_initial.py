# Generated by Django 4.2.9 on 2024-03-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True)),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='fecha de creacion ')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='fecha de modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='fecha de eliminacion')),
            ],
        ),
    ]