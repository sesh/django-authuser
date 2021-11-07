# django-authuser


A reusable custom user model for Django projects.

Includes:

- The user model (email address to sign in, full-name only)
- Sign up form and view
- Logout view with redirect to the homepage
- Admin registration


### Usage

Add the `authuser` app as a git submodule:

```
git submodule add git@github.com:sesh/django-authuser.git authuser
```

Add the app to your `INSTALLED_APPS`, and configure your `AUTH_USER_MODEL` setting:

```
INSTALLED_APPS = [
    ...
    "authuser",
]

AUTH_USER_MODEL = "authuser.User"
```

Add the following to your `settings.py` to allow signups:

```
AUTH_USER_ALLOW_SIGNUP = True
```

Update your `urls.py` in include the signup and logout urls:

```
urlpatterns = [
    ...,
    path('accounts/', include('authuser.urls')),
]
```
