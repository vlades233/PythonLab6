# Generated by Django 2.1.5 on 2019-12-23 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Zabbix_babysize', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_date', models.DateField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Prodact', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Zabbix_babysize',
        ),
        migrations.AddField(
            model_name='server',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zabbix_babysize.ServerCategory'),
        ),
    ]