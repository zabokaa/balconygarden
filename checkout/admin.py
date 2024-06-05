from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    This class represents an inline admin interface for OrderLineItem.
    It is used to display the line item total field in a tabular format
    directly in the Order admin interface.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    # and add it to the OrderAdmin class as an inline


class OrderAdmin(admin.ModelAdmin):
    """"
    This class represents the admin interface for the Order model.
    It is used to display the order number, date, full name, email,
    phone number, country, postcode, town or city, street address1,
    street address2, county, delivery cost, order total, and grand total
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)
# most recent order on top
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
