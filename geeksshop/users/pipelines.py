from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlunparse, urlencode

import requests
from django.utils import timezone
from oauthlib.oauth1.rfc5849.endpoints import access_token
from social_core.exceptions import AuthException, AuthForbidden
from users.models import UserProfile

def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('http', 'api.vk.com', '/method/users.get', None, urlencode(
        OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'personal', 'photo_200')), access_token=response['access_token'],
                    v=5.131)), None))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    if data['sex'] == 1:
        user.userprofile.gender = UserProfile.FEMALE
        user.save()
    elif data['sex'] == 2:
        user.userprofile.gender = UserProfile.MALE
        user.save()
    else:
        pass

    if data['about']:
        user.userprofile.about = data['about']
        user.save()

    if data['personal']:
        user.userprofile.languages = ', '.join(data['personal']['langs'])
        user.save()

    if data['photo_200']:
        user.userprofile.image = data['photo_200']
        user.save()
        # print(user.image)

    bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

    age = timezone.now().date().year-bdate.year
    user.age = age
    if age < 0:
        user.delete()
        raise AuthForbidden('social_core.backends.vk.VKOAuth2')
    user.save()

    # {'alcohol': 0, 'inspired_by': '', 'langs': ['Русский', 'Deutsch', 'English'], 'life_main': 1, 'people_main': 6, 'smoking': 1}