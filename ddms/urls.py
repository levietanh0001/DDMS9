from django.contrib import admin
from django.urls import path, include
from django.apps import apps
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
# local
from .views import base, dashboard, store_dashboard, store_catalogue
from drugs.views import destroy, edit, update, delete_selected, DrugListView, DrugCatalogListView
from members.views import login, logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    # path('', DashBoardListView.as_view(), name='dashboard'),
    path('drug-list/', DrugListView.as_view(), name='drug-list'),
    # path('drug-catalog/', DrugCatalogListView.as_view(), name='drug-catalog'),
    path('drug-catalog/', DrugCatalogListView.as_view(), name='drug-catalog'),
    path('drugs/', include('drugs.urls')),
    path('update/<drug_id>/', update), 
    path('edit/<drug_id>/', edit), 
    path('delete/<drug_id>/', destroy), 
    path('delete_selected/', delete_selected), 
    
    path('accounts/', include('allauth.urls')),
    path('accounts/logout/', logout, name='logout'),
    path('accounts/login/', login, name='login'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('', include(apps.get_app_config('oscar').urls[0])),
    path('catalogue/', RedirectView.as_view(url='/catalogue/'), name='store-catalogue'),
    # path('dashboard/', RedirectView.as_view(url='/dashboard/'), name='store-dashboard'),
    path('dashboard/', store_dashboard, name='store-dashboard'),
    # path('catalogue/', store_catalogue, name='store-catalogue'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
