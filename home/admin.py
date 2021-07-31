from django.contrib import admin
from home.models import *
from home.views import manageemailfromadmin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Recepie)
admin.site.register(FAQ)
#admin.site.register(login_register)
#admin.site.register(review)
admin.site.register(email_verification)
#admin.site.register(guestcart)
#admin.site.register(add_to_cart)
admin.site.register(temporary_order_store)
@admin.register(Today_Special)
class DailySpecial(admin.ModelAdmin):

    def has_add_permission(self, request):
        check = len(Today_Special.objects.all())
        if check == 1:
            return False
        else:
            return True
    def has_delete_permission(self, request, obj=None):
        return False
@admin.register(Featured_product_of_month)
class MonthlySpecial(admin.ModelAdmin):
    def has_add_permission(self, request):
        check = len(Featured_product_of_month.objects.all())
        if check == 1:
            return False
        else:
            return True
    def has_delete_permission(self, request, obj=None):
        return False
@admin.register(Youtube_Link)
class YoutubeLinK(admin.ModelAdmin):

    def has_add_permission(self, request):
        check = len(Youtube_Link.objects.all())
        if check == 1:
            return False
        else:
            return True
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(checkout_order)
class managecheckout(admin.ModelAdmin):
    list_display = ['userid','productid','deliveryaddress','deliverydate','description','quantity','cake_description','payment_method','order_status','phoneno',]
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        manageemailfromadmin(obj.userid.id,obj.order_status)
        return instance



admin.site.site_header = 'Opera Cakes And Bakes'