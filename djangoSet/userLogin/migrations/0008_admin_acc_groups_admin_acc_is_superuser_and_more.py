# Generated by Django 5.0.7 on 2024-10-14 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('userLogin', '0007_alter_admin_acc_dept_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_acc',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='admin_acc_groups', to='auth.group'),
        ),
        migrations.AddField(
            model_name='admin_acc',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='admin_acc',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='admin_acc',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='admin_acc_permissions', to='auth.permission'),
        ),
        migrations.AddField(
            model_name='student_acc',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='student_acc_groups', to='auth.group'),
        ),
        migrations.AddField(
            model_name='student_acc',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='student_acc',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='student_acc',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='student_acc_permissions', to='auth.permission'),
        ),
    ]