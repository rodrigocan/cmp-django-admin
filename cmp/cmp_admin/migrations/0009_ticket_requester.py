# Generated by Django 4.0.3 on 2022-04-01 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp_admin', '0008_remove_ticket_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='requester',
            field=models.CharField(default='Fulano de Tal', max_length=255),
            preserve_default=False,
        ),
    ]
