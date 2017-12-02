# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-02 20:56
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Article Title')),
                ('header', models.TextField(verbose_name='Card Article Preview')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Unique Article Identifier')),
                ('image', models.ImageField(max_length=200, storage=django.core.files.storage.FileSystemStorage(location='E:\\Study\\4_Course(1)\\ControlTheory\\Project\\Project\\static'), upload_to='article_images', verbose_name='Article Image')),
                ('lang', models.CharField(choices=[('en', 'English'), ('ru', 'Russian'), ('uk', 'Ukrainian')], default='uk', max_length=20, verbose_name='Language')),
                ('body', ckeditor.fields.RichTextField(verbose_name='Article Body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Views Count')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='Likes Count')),
                ('dislikes', models.PositiveIntegerField(default=0, verbose_name='Dislikes Count')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'db_table': 'vincent_articles',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ArticleName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(default='', max_length=200, unique=True, verbose_name='Unique Article Name')),
            ],
            options={
                'verbose_name': 'Article Identifier',
                'verbose_name_plural': 'Articles Identifiers',
                'db_table': 'vincent_article_name',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Category Name')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('photo', models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='E:\\Study\\4_Course(1)\\ControlTheory\\Project\\Project\\static'), upload_to='category_photos', verbose_name='Image')),
                ('order_no', models.PositiveIntegerField(unique=True, verbose_name='Order Number')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Ingredient Name')),
                ('photo', models.ImageField(blank=True, default='ingredient_photos/not_found_404.png', null=True, storage=django.core.files.storage.FileSystemStorage(location='E:\\Study\\4_Course(1)\\ControlTheory\\Project\\Project\\static'), upload_to='ingredient_photos', verbose_name='Image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
                'db_table': 'ingredient',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250, verbose_name='Address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('paid', models.BooleanField(default=False, verbose_name='Paid')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'order',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='db.Order')),
            ],
            options={
                'verbose_name': 'OrderItem',
                'verbose_name_plural': 'OrderItems',
                'db_table': 'order_item',
                'ordering': ('product',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Product Name')),
                ('photo', models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='E:\\Study\\4_Course(1)\\ControlTheory\\Project\\Project\\static'), upload_to='product_photos', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Price')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('weight', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='Weight')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='db.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductIngredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='Weight')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Ingredient', verbose_name='Ingredient')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_ingredients', to='db.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Ingredients',
                'verbose_name_plural': 'Product Ingredients',
                'db_table': 'product_ingredients',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Unit Name')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Description')),
                ('short_name', models.CharField(max_length=10, unique=True, verbose_name='Short Value')),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
                'db_table': 'unit',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(through='db.ProductIngredients', to='db.Ingredient', verbose_name='Ingredients'),
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='db.Unit', verbose_name='Unit'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='db.Product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='db.Unit', verbose_name='Unit'),
        ),
        migrations.AddField(
            model_name='article',
            name='unique_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.ArticleName', verbose_name='Article Identifier'),
        ),
        migrations.AlterUniqueTogether(
            name='productingredients',
            unique_together=set([('ingredient', 'product')]),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('unique_name', 'lang')]),
        ),
    ]
