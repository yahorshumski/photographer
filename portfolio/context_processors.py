from .models import Collection, Artwork, Category, Picture


def collections(request):
    """ Add `collections` to RequestContext. """

    return {'collections': Collection.objects.all()}


def artworks(request):
    """ Add `artworks` to RequestContext. """

    return {'artworks': Artwork.objects.all()}


def categories(request):
    """ Add `categories` to RequestContext. """

    return {'categories': Category.objects.all()}


def pictures(request):
    """ Add `categories` to RequestContext. """

    return {'pictures': Picture.objects.all()}
