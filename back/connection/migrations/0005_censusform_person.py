# Generated by Django 4.1.13 on 2023-11-21 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0004_remove_customuser_groups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CensusForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.IntegerField()),
                ('additional_people', models.BooleanField(default=False)),
                ('housing_type', models.CharField(choices=[('ownedWithMortgage', 'Owned by you or someone in this household with a mortgage or loan? Include home equity loans.'), ('ownedWithoutMortgage', 'Owned by you or someone in this household free and clear (without a mortgage or loan)?'), ('rented', 'Rented?'), ('occupiedWithoutRent', 'Occupied without payment of rent?')], max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('age', models.IntegerField()),
                ('birth_month', models.IntegerField()),
                ('birth_day', models.IntegerField()),
                ('birth_year', models.IntegerField()),
                ('hispanic_origin', models.CharField(choices=[('NotHispanic', 'No, not of Hispanic, Latino, or Spanish origin'), ('Mexican', 'Yes, Mexican, Mexican Am., Chicano'), ('PuertoRican', 'Yes, Puerto Rican'), ('Cuban', 'Yes, Cuban'), ('OtherHispanic', 'Yes, another Hispanic, Latino, or Spanish origin')], max_length=20)),
                ('hispanic_origin_text', models.CharField(blank=True, max_length=255, null=True)),
                ('census_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people', to='connection.censusform')),
            ],
        ),
    ]
