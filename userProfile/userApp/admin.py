from email.mime import image
from django.contrib import admin
from userApp.models import UserProfile,Category,Images,title,product,multimage
# Register your models here.

admin.site.register(UserProfile)

#..multiple image
admin.site.register(title)
admin.site.register(product)

#..Gallery...
admin.site.register(Category)
admin.site.register(multimage)
admin.site.register(Images)




