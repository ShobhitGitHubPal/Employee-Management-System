# Generated by Django 4.1.5 on 2023-01-12 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_alter_department_name'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='department',
            table='departments',
        ),
        migrations.AlterModelTable(
            name='employee',
            table='employees',
        ),
        migrations.AlterModelTable(
            name='role',
            table='roles',
        ),
    ]
