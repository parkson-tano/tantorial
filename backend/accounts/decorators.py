from django.http import HttpResponseRedirect


def redirect_authenticated_user_decorator(view):
    """
    A decorator for redirecting logged in users away
    from a view
    """
    def return_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return view(request, *args, **kwargs)
    return return_view
