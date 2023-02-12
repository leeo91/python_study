import admin.my_admin as a

# admin.my_admin.info()
a.info()


from admin import my_admin as b
b.info()


from admin.my_admin import info
info()

