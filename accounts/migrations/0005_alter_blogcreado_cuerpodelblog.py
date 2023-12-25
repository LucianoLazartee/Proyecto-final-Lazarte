from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0004_avatar_delete_usuarioregistrado'),
    ]
    operations = [
        migrations.AlterField(
            model_name='blogcreado',
            name='cuerpoDelBlog',
            field=models.TextField(max_length=500),
        ),
    ]
