# Generated by Django 3.2.8 on 2021-12-20 07:39

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_clothe_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothe',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('M', 'Male'), ('F', 'Female'), ('B', 'Baby'), ('T', 'Traditional'), ('O', 'Modern'), ('C', 'Classic')], default='M', max_length=6),
        ),
        migrations.AlterField(
            model_name='tailor',
            name='gender_spec',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('M', 'Male'), ('F', 'Female'), ('B', 'Baby'), ('T', 'Traditional'), ('O', 'Modern'), ('C', 'Classic')], default='M', max_length=6),
        ),
    ]
