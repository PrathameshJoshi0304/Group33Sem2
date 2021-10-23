from django.contrib import admin

from . models import Contact, BookFirstClass, RegisteredMember,Card, authTrainer, diet, authMember

# Register Tables here
admin.site.register(Contact)
admin.site.register(BookFirstClass)
admin.site.register(RegisteredMember)
admin.site.register(Card)
admin.site.register(authTrainer)
admin.site.register(diet)
admin.site.register(authMember)



