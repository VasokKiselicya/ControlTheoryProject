from django.apps import AppConfig
from material.frontend.apps import ModuleMixin
from django.utils.translation import ugettext_lazy as _


class DbConfig(ModuleMixin, AppConfig):
    name = 'db'
    icon = '<i class="material-icons">store</i>'
    verbose_name = _('App Config')
