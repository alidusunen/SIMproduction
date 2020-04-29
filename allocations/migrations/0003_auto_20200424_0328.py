# Generated by Django 3.0.5 on 2020-04-24 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0002_allocation_assets'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allocation',
            old_name='allocation_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='allocation',
            old_name='document_number',
            new_name='documentNumber',
        ),
        migrations.RenameField(
            model_name='allocation',
            old_name='new_program',
            new_name='newBudget',
        ),
        migrations.RenameField(
            model_name='allocation',
            old_name='new_donor',
            new_name='newDonor',
        ),
        migrations.RenameField(
            model_name='allocation',
            old_name='previous_budget',
            new_name='previousBudget',
        ),
        migrations.RenameField(
            model_name='allocation',
            old_name='previous_donor',
            new_name='previousDonor',
        ),
    ]