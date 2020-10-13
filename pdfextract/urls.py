from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/v1/create/', views.CreateView.as_view(), name='create'),
    path('api/v1/check/<int:id>/', views.CheckStatus.as_view(), name='check')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
