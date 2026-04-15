from django.http import HttpResponsePermanentRedirect


class WwwRedirectMiddleware:
    """Permanently redirect www.pixelmonks.com → pixelmonks.com."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(":")[0]  # strip port if present
        if host.startswith("www."):
            bare = host[4:]
            return HttpResponsePermanentRedirect(
                f"https://{bare}{request.get_full_path()}"
            )
        return self.get_response(request)
