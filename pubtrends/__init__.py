from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('api', '/api/')
    config.add_route('api_pub_per_year', '/api/per_year/')
    config.add_route('api_locations', '/api/locations/')

    config.add_route('viewer', '/viewer/')
    config.add_route('home', '/')

    config.add_route('map', '/map/')
    config.scan()
    return config.make_wsgi_app()
