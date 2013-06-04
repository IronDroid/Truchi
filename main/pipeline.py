from django.core.files import File
from main.models import Estudiante
import urllib2

def get_user_avatar(backend, details, response, social_user, uid, user, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
 
    elif backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal', '')

    if url:
        userest = Estudiante()
        userest.username = user
        userest.nombre = details['first_name'] +" "+ details['last_name']
        userest.email = details['email']
        userest.avatar = url
        userest.social_network = backend.name

        # content = urllib2.urlopen(url)
        # nombre_avatar = url.split('/')[-1]
        # userest.avatar.save(nombre_avatar, File(open(content[0])), save=True)

        userest.save()