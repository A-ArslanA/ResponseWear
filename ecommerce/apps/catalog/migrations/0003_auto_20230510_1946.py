# Generated by Django 3.2 on 2023-05-10 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20230307_1838'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категориялар'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',), 'verbose_name': 'Тауар', 'verbose_name_plural': 'Тауарлар'},
        ),
    ]
