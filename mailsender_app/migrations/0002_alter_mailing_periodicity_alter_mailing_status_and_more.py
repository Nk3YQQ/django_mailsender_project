# Generated by Django 5.0.4 on 2024-04-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailsender_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='periodicity',
            field=models.CharField(choices=[('Раз в день', 'Раз в день'), ('Раз в неделю', 'Раз в неделю'), ('Раз в месяц', 'Раз в месяц')], max_length=30, verbose_name='Периодичность'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('Завершена', 'Завершена'), ('Создана', 'Создана'), ('Запущена', 'Запущена')], default='Запущена', max_length=30, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовок'),
        ),
    ]