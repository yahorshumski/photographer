from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import patterns, include, url

from surlex.dj import surl
from django.contrib import admin



from .views import (
    HomeView,
    ArtworkDetailView, ArtworkListView,
    CollectionListView, CollectionDetailView,
    CategoryListView, CategoryDetailView
)


urlpatterns = patterns('',
    # Home view
    surl(r'^$', HomeView.as_view(),
        name='portfolio_home'
    ),

    # Collection views
    surl(r'^collections/$', CollectionListView.as_view(),
        name='collection_list'
    ),
    surl(r'^collections/<slug:s>/', CollectionDetailView.as_view(),
        name='collection_detail'
    ),

    # Artwork views
    surl(r'^works/$', ArtworkListView.as_view(),
        name='artwork_list'
    ),
    surl(r'^works/<pk:#>/$', ArtworkDetailView.as_view(),
        name='artwork_detail'
    ),

    # Category views
    surl(r'^category/$', CategoryListView.as_view(),
        name='category_list'
    ),
    surl(r'^category/<slug:s>/', CategoryDetailView.as_view(),
        name='category_detail'
    ),

    url(r'^admin/', include(admin.site.urls)),


    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
)
