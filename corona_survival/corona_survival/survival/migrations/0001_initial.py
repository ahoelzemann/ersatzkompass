# Generated by Django 2.2.5 on 2020-03-21 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='survival.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Substitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_of_creation', models.TextField(blank=True)),
                ('item_missing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='survival.Item')),
                ('items_needed', models.ManyToManyField(related_name='items_needed', to='survival.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='survival.Category')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='survival.Subcategory'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True)),
                ('substitution', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='survival.Substitution')),
            ],
        ),
    ]
