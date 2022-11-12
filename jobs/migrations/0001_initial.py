# Generated by Django 4.1.2 on 2022-11-02 21:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('selected_store', models.CharField(max_length=200)),
                ('selected_brand', models.CharField(max_length=200)),
                ('selected_product', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('tm_stamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]