from django.views.generic import ListView, DetailView, RedirectView
from django.core.urlresolvers import reverse

from .models import Artwork, Category, Collection, Picture


class HomeView(RedirectView):
    """ Home view redirects to collection list. """
    permanent = True

    def get_redirect_url(self, **kwargs):
        return reverse('collection_list')


class ArtworkViewBase(object):
    model = Artwork


class ArtworkDetailView(ArtworkViewBase, DetailView):
    pass


class ArtworkListView(ArtworkViewBase, ListView):
    pass


class CollectionViewBase(object):
    model = Collection



class CollectionDetailView(CollectionViewBase, DetailView):
    pass


class CollectionListView(CollectionViewBase, ListView):

    def Picture(self):
        return Picture.objects.all()


class CategoryViewBase(object):
    model = Category


class CategoryDetailView(CategoryViewBase, DetailView):
    pass


class CategoryListView(CategoryViewBase, ListView):
    pass
