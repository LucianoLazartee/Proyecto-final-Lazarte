from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emisor', models.EmailField(max_length=254)),
                ('receptor', models.EmailField(max_length=254)),
                ('cuerpoDelMensaje', models.CharField(max_length=250)),
            ],
        ),
    ]
