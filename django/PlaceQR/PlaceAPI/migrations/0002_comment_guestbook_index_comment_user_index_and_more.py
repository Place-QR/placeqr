# Generated by Django 4.1.3 on 2022-11-13 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlaceAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='guestbook_index',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PlaceAPI.guestbook'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_index',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PlaceAPI.user'),
        ),
        migrations.AddField(
            model_name='guestbook',
            name='user_index',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PlaceAPI.user'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
