from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0005_alter_blogcreado_cuerpodelblog'),
    ]
    operations = [
        migrations.AlterField(
            model_name='blogcreado',
            name='cuerpoDelBlog',
            field=models.TextField(),
        ),
    ]
