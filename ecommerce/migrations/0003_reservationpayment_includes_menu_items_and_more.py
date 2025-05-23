# Generated by Django 5.2 on 2025-05-01 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_reservation_has_menu_items_reservation_prepare_ahead'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationpayment',
            name='includes_menu_items',
            field=models.BooleanField(default=True, help_text='Whether this payment includes pre-ordered menu items'),
        ),
        migrations.CreateModel(
            name='ReservationItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('special_instructions', models.TextField(blank=True)),
                ('inventory_updated', models.BooleanField(default=False)),
                ('is_prepared', models.BooleanField(default=False, help_text='Whether this item has been prepared')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.menuitem')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_items', to='ecommerce.reservation')),
            ],
            options={
                'ordering': ['reservation', 'menu_item'],
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='items',
            field=models.ManyToManyField(through='ecommerce.ReservationItem', to='ecommerce.menuitem'),
        ),
    ]
