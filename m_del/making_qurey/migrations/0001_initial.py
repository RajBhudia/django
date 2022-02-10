# Generated by Django 4.0 on 2022-02-09 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=60)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_name', models.CharField(max_length=100)),
                ('tech_contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=100)),
                ('stu_id', models.IntegerField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='making_qurey.subject')),
                ('subject_tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='making_qurey.teacher')),
            ],
        ),
    ]
