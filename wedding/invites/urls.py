from django.conf.urls import url
from .views import RSVPLookupView, RSVPView, RSVPThanksView

urlpatterns = [
    url(
        regex=r'^$',
        view=RSVPLookupView.as_view(),
        name='RSVPLookupView'
    ),
    url(
        regex=r'^(?P<hashid>\w+)/$',
        view=RSVPView.as_view(),
        name='RSVPView'
    ),

    url(
        regex=r'thanks$',
        view=RSVPThanksView.as_view(),
        name='RSVPThanks'
    ),
]
