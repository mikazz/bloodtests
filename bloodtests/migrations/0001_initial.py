# Generated by Django 2.2.14 on 2022-11-05 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=10)),
                ('lower', models.FloatField(blank=True, default=None, null=True)),
                ('upper', models.FloatField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'bloodtests_testresult',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('testresult_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bloodtests.TestResult')),
            ],
            bases=('bloodtests.testresult',),
        ),
        migrations.AddConstraint(
            model_name='testresult',
            constraint=models.CheckConstraint(check=models.Q(lower__gte=0.0), name='lower_range_constraint'),
        ),
        migrations.AddConstraint(
            model_name='testresult',
            constraint=models.CheckConstraint(check=models.Q(upper__gte=0.0), name='upper_range_constraint'),
        ),
    ]
