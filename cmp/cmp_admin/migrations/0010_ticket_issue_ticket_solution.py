# Generated by Django 4.0.3 on 2022-04-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp_admin', '0009_ticket_requester'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='issue',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='solution',
            field=models.TextField(blank=True),
        ),
    ]
