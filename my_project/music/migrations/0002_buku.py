# Generated by Django 3.2 on 2022-03-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=45)),
                ('pengarang', models.CharField(max_length=45)),
                ('tanggal_rilis', models.DateField()),
                ('gambar', models.ImageField(upload_to='buku')),
            ],
            options={
                'db_table': 'judul',
            },
        ),
    ]
