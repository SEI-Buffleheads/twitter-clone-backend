from django.urls import path
from .views import RegisterView, LoginAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# schema_view = get_schema_view(
#    openapi.Info(
#       title="Twitter Backend API",
#       default_version='v1',
#       description="ghetto twitter api",
#       terms_of_service="Don't steal",
#       contact=openapi.Contact(email="@faketwitterapi"),
#       license=openapi.License(name="Tony License  "),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )

urlpatterns = [
  # path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
  # path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  path('register/', RegisterView.as_view(), name='register'),
  path('login/', LoginAPIView.as_view(), name='login')
]