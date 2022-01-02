# Generated by Django 3.2.8 on 2021-12-18 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tailor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.IntegerField(null=True)),
                ('gender_spec', multiselectfield.db.fields.MultiSelectField(choices=[('M', 'Male'), ('F', 'Female'), ('B', 'Baby'), ('T', 'Traditional'), ('M', 'Modern'), ('C', 'Classic')], default='M', max_length=6)),
                ('location', models.TextField(null=True)),
                ('size', models.IntegerField(default=1)),
                ('rating', models.IntegerField(choices=[(1, 'Bad'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.IntegerField(null=True)),
                ('address', models.TextField(null=True)),
                ('gen_size', models.IntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[('M', 'Male'), ('F', 'Female'), ('B', 'Baby'), ('T', 'Traditional'), ('M', 'Modern'), ('C', 'Classic')], default='M', max_length=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image', models.ImageField(upload_to=main.models.cloth_image_path)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tailor')),
            ],
        ),
    ]
