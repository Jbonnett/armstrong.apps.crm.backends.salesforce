from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.test.client import RequestFactory
import unittest
from ._utils import TestCase

try:
    from registration.backends import default as registration
    from registration.signals import user_activated
    from registration.signals import user_registered
    from registration.models import RegistrationProfile
except ImportError:
    user_activated, user_registered = False, False

from .. import base

def random_user():
    return User.objects.create(username='testuser-%d' % random.randint() )

class SalesForceTestCase(TestCase):
    def setUp(self):
        with self.settings(ARMSTRONG_CRM_BACKEND="armstrong.apps.crm.backends.salesforce" ):
            self.b = base.get_backend()
    
    def test_dispatches_user_create(self):
        random_user()
        pass

    def test_dispatches_user_update(self):
        pass

    def test_dispatch_user_delete(self):
        pass

    def test_dispatches_group_create(self):
        pass

    def test_dispatches_group_update(self):
        pass

    def test_dispatch_group_delete(self):
        pass

    @unittest.skipIf(user_activated is False,
            "django-registration is not installed")
    def test_activate_signal_if_available(self):
        pass

