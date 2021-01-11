# Generated by Django 3.0.5 on 2021-01-11 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transcribe_audio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QADataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('transcript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcribe_audio.AudioDataModel')),
            ],
        ),
    ]
