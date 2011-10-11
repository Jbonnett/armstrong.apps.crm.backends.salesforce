from django.conf import settings

from sforce.enterprise import SforceEnterpriseClient

def get_connection(): 
    h = SforceEnterpriseClient(settings.SFORCE_WSDL_PATH)
    h.login(settings.SFORCE_USER, settings.SFORCE_PASSWORD, settings.SFORCE_TOKEN)
    return h