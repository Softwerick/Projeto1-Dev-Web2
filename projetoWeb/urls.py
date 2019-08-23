from django.contrib import admin
from django.urls import path
from market import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table/', views.table, name='table'),
    path('signup/', views.signup, name="submit"),
    path('',views.homepage, name="index"),
    path('table/<name>',views.product_detail, name='product'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('new_product/', views.create_product, name='create_product')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
