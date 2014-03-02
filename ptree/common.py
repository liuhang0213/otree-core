import babel.numbers
from django.conf import settings
from decimal import Decimal
import urllib
import urlparse
from django.utils.importlib import import_module
import subprocess
from django.template.defaultfilters import title
from ptree import constants

def add_params_to_url(url, params):
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urllib.urlencode(query)
    return urlparse.urlunparse(url_parts)

def id_label_name(id, label):
    if label:
        return '{} (label: {})'.format(id, label)
    return '{}'.format(id)

def currency(value):
    """Takes in a number of cents (int) and returns a formatted currency amount.
    """

    if value == None:
        return '?'
    value_in_major_units = Decimal(value)/(10**settings.CURRENCY_DECIMAL_PLACES)
    return babel.numbers.format_currency(value_in_major_units, settings.CURRENCY_CODE, locale=settings.CURRENCY_LOCALE)

def create_match(MatchClass, treatment):
    match = MatchClass(treatment = treatment,
                       subsession = treatment.subsession,
                       session = treatment.session)
    # need to save it before you assign the participant.match ForeignKey
    match.save()
    return match

def is_subsession_app(app_label):
    try:
        models_module = import_module('{}.models'.format(app_label))
    except ImportError:
        return False
    class_names = ['Participant', 'Match', 'Treatment', 'Subsession']
    return all(hasattr(models_module, ClassName) for ClassName in class_names)

def git_hash():
    '''fixme: seems not to be working'''
    try:
        hash = subprocess.check_output(['git rev-parse HEAD'.split()])
    except:
        return None
    try:
        subprocess.check_call('git diff-index --quiet HEAD')
        return hash
    except subprocess.CalledProcessError:
        return '{} (plus uncommitted changes)'.format(hash)

def app_name_format(app_name):
    return title(app_name.replace("_", " "))

def url(cls, session_user, index=None):
    u = '/{}/{}/{}/{}/'.format(
        session_user.user_type_in_url,
        session_user.code,
        cls.get_name_in_url(),
        cls.__name__,
    )

    if index is not None:
        u += '{}/'.format(index)
    return u

def url_pattern(cls, is_sequence_url=False):
    p = r'(?P<{}>\w)/(?P<{}>[a-z]+)/{}/{}/'.format(
        constants.user_type,
        constants.session_user_code,
        cls.get_name_in_url(),
        cls.__name__,
    )
    if is_sequence_url:
        p += '\d+/'
    p = '^{}$'.format(p)
    return p
