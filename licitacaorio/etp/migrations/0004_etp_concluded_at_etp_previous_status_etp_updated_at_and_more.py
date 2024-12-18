# Generated by Django 5.1.2 on 2024-10-25 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etp', '0003_etp_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='etp',
            name='concluded_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='etp',
            name='previous_status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Concluído', 'Concluído')], default='Pendente', max_length=9),
        ),
        migrations.AddField(
            model_name='etp',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='etp',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Concluído', 'Concluído')], default='Pendente', max_length=9),
        ),
    ]
