from django.urls import path
from housing.views import *

app_name = 'housing'

urlpatterns = [
    path('export-progress/', export_progress_to_excel, name='export_progress_to_excel'),
    # ------------ COMUNIDADES ---------------
    path('communities/', CommunitiesView.as_view(), name='communities'),
    path('create_communities/', CreateCommunities.as_view(), name='create_communities'),
    path('communities/<int:pk>/edit/', EditCommunities.as_view(), name='edit_communities'),
    path('communities/<int:pk>/delete/', DeleteCommunity.as_view(), name='delete_community'),

    # ------------ PROGRESOS ---------------
    path('progress/', ProgressCommunitiesView.as_view(), name='progress'), #lista todas las comunidades
    path('progress/<int:pk>/', ComunidadDetailView.as_view(), name='comunidad_detail'), #lista los representantes de la comunidad seleccionada
    
    path('progress/<int:community_pk>/familia/<int:representante_id>/progresos/', ProgresoViviendaListView.as_view(), name='progreso_vivienda'),
    path('progress/<int:community_pk>/familia/<int:representante_id>/progresos/agregar/', AgregarProgresoView.as_view(), name='agregar_progreso'),
    path('progress/<int:community_pk>/familia/<int:representante_id>/progresos/<int:pk>/detalle/', ProgresoViviendaDetailView.as_view(), name='detalle_progreso'),
    path('progress/<int:community_pk>/familia/<int:representante_id>/progresos/<int:pk>/editar/', ProgresoViviendaUpdateView.as_view(), name='editar_progreso'),
    path('progress/<int:community_pk>/familia/<int:representante_id>/progresos/<int:pk>/eliminar/', ProgresoViviendaDeleteView.as_view(), name='eliminar_progreso'),
    path('progress/<int:community_pk>/familia/<int:representante_id>/progresos/<int:pk>/exportar-pdf/', generar_pdf_progreso, name='generar_pdf_progreso'),


    # ------------ FAMILIAS ---------------
    path('families/', FamiliesView.as_view(), name='families'),
    path('create_families/', CreateFamilies.as_view(), name='create_families'),
    path('families/<int:pk>/edit/', EditFamilies.as_view(), name='edit_families'),
    path('families/<int:pk>/delete/', DeleteFamily.as_view(), name='delete_family'),
]