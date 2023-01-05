# Generated by Django 4.0.5 on 2022-12-31 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=200)),
                ('session', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('semester', models.CharField(choices=[('First', 'First'), ('Second', 'Second')], default='First', max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]