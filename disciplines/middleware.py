from django.http import HttpResponsePermanentRedirect

class RedirectToPrimaryDomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host == 'kuisk.herokuapp.com':
            return HttpResponsePermanentRedirect('https://www.kuisk.com' + request.path_info)
        return self.get_response(request)
