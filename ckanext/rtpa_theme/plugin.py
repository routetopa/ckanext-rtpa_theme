import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Rtpa_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    # IConfigurer
    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'rtpa_theme')

    ## IRoutes
    def before_map(self, map):
        controller = 'ckanext.rtpa_theme.controllers:ViewController'
        map.redirect('/', '/dataset')
        return map