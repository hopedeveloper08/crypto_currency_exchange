# Generated by Django 4.2 on 2024-06-04 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_buy', models.BooleanField()),
                ('amount', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.currency')),
                ('trader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]