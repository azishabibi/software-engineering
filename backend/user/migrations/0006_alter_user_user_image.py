# Generated by Django 4.2.5 on 2023-11-16 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_alter_user_gender_alter_user_nickname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_image",
            field=models.ImageField(null=True, upload_to="", verbose_name="用户头像"),
        ),
    ]
