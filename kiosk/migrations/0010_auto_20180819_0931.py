# Generated by Django 2.1 on 2018-08-19 14:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk', '0009_artifact_file_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscussionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('discussion_subject', models.CharField(blank='True', max_length=1250)),
                ('discussion_text', models.CharField(max_length=2000)),
                ('created_date', models.DateTimeField(blank='True', default=django.utils.timezone.now, verbose_name='publish time')),
            ],
        ),
        migrations.AddField(
            model_name='artifact',
            name='discussion_items',
            field=models.ForeignKey(blank='True', null=True, on_delete=django.db.models.deletion.CASCADE, to='kiosk.DiscussionItem'),
        ),
        migrations.AddField(
            model_name='project',
            name='discussion_items',
            field=models.ForeignKey(blank='True', null=True, on_delete=django.db.models.deletion.CASCADE, to='kiosk.DiscussionItem'),
        ),
    ]