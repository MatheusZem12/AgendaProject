# Generated by Django 3.2.25 on 2025-02-04 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20250204_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelTable(
            name='contact',
            table=('tb_contact',),
        ),
    ]
