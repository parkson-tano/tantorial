from django.http import HttpResponseRedirect


class RedirectAuthenticatedUserMixin:
    """
    Redirects authenticated users to a specified url.
    By default it redirect the user to the home page
    """
    redirect_user_to_url = "/"  # can be used to change redirect url

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.redirect_user_to_url)
        return super().dispatch(request, *args, **kwargs)
