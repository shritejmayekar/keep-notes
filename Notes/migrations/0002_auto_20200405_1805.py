# Generated by Django 2.2.2 on 2020-04-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'ordering': ['-sort_order', '-created_at'], 'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
        migrations.AddField(
            model_name='notes',
            name='color',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
