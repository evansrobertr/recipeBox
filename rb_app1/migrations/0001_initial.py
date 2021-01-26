# Generated by Django 2.2 on 2021-01-16 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_name', models.CharField(max_length=255)),
                ('box_color', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=255)),
                ('notes', models.TextField(null=True)),
                ('recipe_author', models.CharField(max_length=60)),
                ('recipe_type', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=100)),
                ('password_confirm', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('user_description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('step_for_recipe', models.ManyToManyField(related_name='recipe_step', to='rb_app1.Recipes')),
            ],
        ),
        migrations.AddField(
            model_name='recipes',
            name='collected_recipe',
            field=models.ManyToManyField(related_name='user_recipe', to='rb_app1.Users'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='in_box',
            field=models.ManyToManyField(related_name='recipe_card', to='rb_app1.Boxes'),
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('in_recipe', models.ManyToManyField(related_name='recipe_ingredients', to='rb_app1.Recipes')),
            ],
        ),
        migrations.AddField(
            model_name='boxes',
            name='box_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_box', to='rb_app1.Users'),
        ),
    ]