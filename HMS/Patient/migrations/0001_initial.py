# Generated by Django 4.2.5 on 2023-09-29 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='User.user')),
                ('patientID', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('User.user',),
        ),
    ]
