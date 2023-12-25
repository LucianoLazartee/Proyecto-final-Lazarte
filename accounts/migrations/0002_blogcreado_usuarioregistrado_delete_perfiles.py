from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='BlogCreado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloDelBlog', models.CharField(max_length=50, unique=True)),
                ('subtituloDelBlog', models.CharField(max_length=100)),
                ('cuerpoDelBlog', models.CharField(max_length=1000)),
                ('autorDelBlog', models.CharField(max_length=50)),
                ('fechaDelBlog', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioRegistrado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDeUsuario', models.CharField(max_length=20, unique=True)),
                ('contrasena', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='perfiles',
        ),
    ]
