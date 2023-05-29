# Generated by Django 3.2.4 on 2023-05-15 10:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=100)),
                ('product_category_image', models.ImageField(upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=5000)),
                ('answer', models.TextField(max_length=15000)),
            ],
        ),
        migrations.CreateModel(
            name='login_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=10)),
                ('email_address', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=40)),
                ('date_registered', models.DateField(default=datetime.datetime(2023, 5, 15, 10, 7, 28, 972401, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.PositiveIntegerField()),
                ('product_short_description', models.TextField(max_length=150)),
                ('product_long_description', models.TextField(max_length=300)),
                ('image1', models.ImageField(upload_to='product')),
                ('image2', models.FileField(blank=True, null=True, upload_to='product')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='product')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Recepie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recepie_name', models.CharField(max_length=200)),
                ('recepie_description', models.TextField(max_length=500)),
                ('recepie_ingredients', models.TextField(help_text="Use ',' to seperate ingredients", max_length=5000)),
                ('recepie_direction', models.TextField(max_length=10000)),
                ('final_image', models.ImageField(upload_to='recepie')),
            ],
        ),
        migrations.CreateModel(
            name='Youtube_Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Youtube_Link', models.CharField(max_length=9000)),
            ],
        ),
        migrations.CreateModel(
            name='Today_Special',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product1', to='home.product')),
                ('product_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product2', to='home.product')),
                ('product_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product3', to='home.product')),
            ],
        ),
        migrations.CreateModel(
            name='temporary_order_store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=400)),
                ('deliveryaddress', models.CharField(max_length=400)),
                ('deliverydate', models.DateField()),
                ('phoneno', models.CharField(max_length=10)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.login_register')),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=110)),
                ('reviewdate', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.login_register')),
            ],
        ),
        migrations.CreateModel(
            name='guestcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guestuser', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField()),
                ('description', models.TextField(default='No description')),
                ('cake_description', models.CharField(default='Not a cake!', max_length=400)),
                ('create_date', models.DateField(default=datetime.datetime(2023, 5, 15, 10, 7, 28, 973401, tzinfo=utc))),
                ('cartproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
        migrations.CreateModel(
            name='Featured_product_of_month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_of_month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
        migrations.CreateModel(
            name='email_verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=250)),
                ('verify', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.login_register')),
            ],
        ),
        migrations.CreateModel(
            name='checkout_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordername', models.CharField(max_length=200)),
                ('deliveryaddress', models.CharField(max_length=200)),
                ('deliverydate', models.DateField()),
                ('phoneno', models.CharField(max_length=10)),
                ('quantity', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=400)),
                ('cake_description', models.CharField(max_length=400)),
                ('payment_method', models.CharField(default='Home Delivery', max_length=150)),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel Order', 'Cancel Order')], default='Pending', max_length=30)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.login_register')),
            ],
        ),
        migrations.CreateModel(
            name='add_to_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('description', models.TextField(default='No description')),
                ('cake_description', models.CharField(default='Not a cake!', max_length=400)),
                ('create_date', models.DateField(default=datetime.datetime(2023, 5, 15, 10, 7, 28, 972401, tzinfo=utc))),
                ('cartproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
                ('cartuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.login_register')),
            ],
        ),
    ]
