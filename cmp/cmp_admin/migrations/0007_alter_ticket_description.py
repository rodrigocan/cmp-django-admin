# Generated by Django 4.0.3 on 2022-04-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp_admin', '0006_status_remove_ticket_service_ticket_status_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(),
        ),
    ]
