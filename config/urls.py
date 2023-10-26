from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

schema_view = get_schema_view(
    openapi.Info(
        title="CRM API",
        default_version='v1',
        description="API of CRM for education and training centres",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ravshanovdaler06@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('school/', include('schools.urls')),
    path('users/', include('users.urls'))
]

urlpatterns += staticfiles_urlpatterns()
