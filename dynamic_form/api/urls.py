from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name="index"),
    path('form/', views.FormView.as_view(), name='create_or_update_form'),
    path('form/<slug:form_id>', views.FormView.as_view(), name='create_or_update_form'),
    path('form/response/<slug:form_id>', views.ResponseView.as_view(), name="form_response"),
    path('get/form/response/<slug:response_id>', views.ResponseView.as_view(), name="form_response")
]
