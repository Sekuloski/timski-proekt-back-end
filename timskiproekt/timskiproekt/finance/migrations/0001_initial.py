# Generated by Django 4.2.3 on 2023-07-12 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('addition_type', models.IntegerField(choices=[(0, 'Salary'), (1, 'ATM'), (2, 'Sale')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('expense_type', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='finance.expensetype')),
            ],
        ),
    ]