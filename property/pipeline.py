from social_django.models import UserSocialAuth
from .models import User


def get_avatar(backend, response, user=None, *args, **kwargs):
    url = None
    print(user.id)
    request_user = User.objects.get_or_create(id=user.id)
    if backend.name == "yandex-oauth2":
        print(response)
        default_avatar_id = response.get("default_avatar_id", "")
        first_name = response.get("first_name", "")
        last_name = response.get("last_name", "")
        email = response.get("default_email", "")
        if default_avatar_id:
            url = (
                f"https://avatars.yandex.net/get-yapic/{default_avatar_id}/islands-200"
            )    
    if backend.name == "google-oauth2":
        print(response)
        url = response.get("picture", "")
        url = url.replace("96-c", "200-c")
        first_name = response.get("given_name", "")
        last_name = response.get("family_name", "")
        email = response.get("email", "")
    if url:
        request_user[0].user = user.username
        request_user[0].url = url
        request_user[0].first_name = first_name
        request_user[0].last_name = last_name
        request_user[0].email = email
        request_user[0].save()

