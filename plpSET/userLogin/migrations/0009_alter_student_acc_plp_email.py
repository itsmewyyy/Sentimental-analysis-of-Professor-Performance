# Generated by Django 5.0.7 on 2024-10-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userLogin', '0008_admin_acc_groups_admin_acc_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_acc',
            name='plp_email',
            field=models.EmailField(default='example_example@plpasig.edu.ph', max_length=254, unique=True),
        ),
    ]