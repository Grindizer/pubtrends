from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest

from queries import queries
from datetime import date

@view_config(route_name='viewer', renderer='templates/viewer.pt')
def my_view(request):
    return {}

@view_config(route_name='map', renderer='templates/map.pt')
def map(request):
    return {}

@view_config(route_name='api_pub_per_year', renderer='json')
def api_pub_per_year(request):
    # check and validate values.
    try:
        start, stop, term = search_form_validate(request.GET)
    except ValueError:
        raise HTTPBadRequest("Form Validation Failed")

    return list(queries.pubmed_count_per_year(start, stop, term))

@view_config(route_name='api_locations', renderer='json')
def api_locations(request):
    try:
        start, stop, term = search_form_validate(request.GET)
    except ValueError:
        raise HTTPBadRequest("Form Validation Failed")

    return list(queries.pubmed_locations(start, stop, term))

def search_form_validate(data):
    start = data.get('start', None)
    stop = data.get('stop', None)
    term = data.get('term', None)

    start, stop = int(start), int(stop)

    if not start or start < 1951:
        start = 1951

    if not stop or stop > date.today().year:
        stop = date.today().year

    if not term:
        raise ValueError("term cannot be empty")

    return start, stop, term
