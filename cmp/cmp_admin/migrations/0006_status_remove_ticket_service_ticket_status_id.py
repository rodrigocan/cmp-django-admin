# Generated by Django 4.0.3 on 2022-04-01 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmp_admin', '0005_subject_service_ticket_service_id_ticket_subject_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='service',
        ),
        migrations.AddField(
            model_name='ticket',
            name='status_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmp_admin.status'),
        ),
    ]
