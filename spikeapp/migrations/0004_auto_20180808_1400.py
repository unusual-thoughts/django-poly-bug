# Generated by Django 2.0.1 on 2018-08-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spikeapp', '0003_auto_20180808_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128)),
                ('lastname', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'SEPA beneficiary',
                'verbose_name_plural': 'SEPA Beneficiaries',
            },
        ),
        migrations.AddField(
            model_name='sepapayment',
            name='destination',
            field=models.ManyToManyField(related_name='sepa', to='spikeapp.Beneficiary'),
        ),
    ]
