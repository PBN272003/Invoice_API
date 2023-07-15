from django.urls import include, path
from rest_framework.routers import DefaultRouter
from invoices import views
from django.contrib  import admin
router = DefaultRouter()
router.register('invoices', views.InvoiceViewSet,basename='invoices')
router.register('invoicedetails', views.InvoiceDetailViewSet,basename='invoicedetails')

urlpatterns = [
    # other URL patterns for your project
    path('admin/',admin.site.urls),
    path('api/', include(router.urls)),
]