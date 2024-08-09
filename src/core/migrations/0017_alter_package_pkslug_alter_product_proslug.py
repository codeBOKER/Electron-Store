# Generated by Django 4.2.14 on 2024-07-30 19:46

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_package_pkslug_alter_product_proslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='PkSlug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProSlug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]
