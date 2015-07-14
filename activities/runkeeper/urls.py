from django.conf.urls import patterns, url

from .views import DataRetrievalView, DisconnectView, FinalizeImportView


urlpatterns = patterns(
    '',

    url(r'^finalize-import/$',
        FinalizeImportView.as_view(),
        name='finalize-import'),

    url(r'^disconnect/$',
        DisconnectView.as_view(),
        name='disconnect'),

    url(r'^request-data-retrieval/$',
        DataRetrievalView.as_view(),
        name='request-data-retrieval'),
)