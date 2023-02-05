# Generated by Django 4.1.5 on 2023-01-30 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_productmodel_sale_alter_sizemodel_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='wishlist', to='products.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='wishlist', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'wishlist',
                'verbose_name_plural': 'wishlists',
                'unique_together': {('user', 'product')},
            },
        ),
    ]