from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import  views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('', include('mainapp.urls')),
    path('assessment/', include('assessment.urls')),
    path('accounts/', include('accounts.urls')),
     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='forgotpassword/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="forgotpassword/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='forgotpassword/password_reset_complete.html'), name='password_reset_complete')
]
urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 