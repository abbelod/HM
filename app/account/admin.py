from django.contrib import admin
from .models import Plan, Subscription, StripeCustomer, User

admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(StripeCustomer)
admin.site.register(User)
