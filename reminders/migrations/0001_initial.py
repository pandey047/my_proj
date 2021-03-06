# Generated by Django 3.2.7 on 2021-12-02 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deals', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(blank=True, max_length=300, null=True, verbose_name='Notes')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('complete', 'complete'), ('snooze', 'snooze')], default='pending', max_length=50, verbose_name='Status')),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('dismissed_at', models.DateTimeField(blank=True, null=True, verbose_name='Dismissed At')),
                ('snooze', models.DateTimeField(blank=True, null=True, verbose_name='Snooze')),
                ('deal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deals.deal')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
