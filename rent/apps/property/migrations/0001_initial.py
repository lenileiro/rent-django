# Generated by Django 2.2.4 on 2019-08-10 22:34

from django.db import migrations, models
import django.db.models.deletion
import rent.apps.property.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('property_id', models.AutoField(primary_key=True, serialize=False)),
                ('property_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_number', models.CharField(max_length=255)),
                ('floor', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('picture', models.ImageField(blank=True, upload_to=rent.apps.property.models.get_image_path)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='property.Property')),
            ],
        ),
    ]
