# Generated by Django 5.1.2 on 2024-10-29 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_category_contact_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]