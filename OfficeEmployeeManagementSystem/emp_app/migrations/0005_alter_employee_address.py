# Generated by Django 4.2.3 on 2024-10-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0004_delete_department_delete_role_employee_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(blank=True, help_text='Enter the full address', null=True),
        ),
    ]
