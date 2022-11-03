# Generated by Django 4.1.2 on 2022-11-03 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0005_alter_post_created_by'),
        ('comments', '0002_alter_comment_options_alter_comment_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagAtPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=20)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
            options={
                'unique_together': {('content',)},
            },
        ),
        migrations.CreateModel(
            name='TagAtComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=20)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.comment')),
            ],
            options={
                'unique_together': {('content',)},
            },
        ),
    ]
