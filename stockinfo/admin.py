from django.contrib import admin
from .models import Stock,Portfolio,Holding,Transaction

admin.site.register(Stock)
admin.site.register(Portfolio)
admin.site.register(Holding)
admin.site.register(Transaction)

