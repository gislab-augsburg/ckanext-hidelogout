import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class HideLogoutButtonPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')

    def get_helpers(self):
        return {
            'should_hide_logout_button': self.should_hide_logout_button
        }

    def should_hide_logout_button(self):
        config = toolkit.config
        return config.get('ckan.hide_logout_button', 'false').lower() == 'true'
