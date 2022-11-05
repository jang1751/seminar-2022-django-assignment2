# Generated by Django 4.1.2 on 2022-11-05 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0004_alter_tag_content'),
        ('comments', '0004_alter_comment_post_alter_comment_written_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagToComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.comment')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.tag')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='tags',
            field=models.ManyToManyField(through='comments.TagToComment', to='tags.tag'),
        ),
    ]
