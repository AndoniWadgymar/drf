from django.http import JsonResponse
import json

# Create your views here.
def api_home(request, *args, **kwargs):
  #request -> HttpRequest -> Django
  #request.body
  body = request.body #byte string of JSON body
  data = {}
  try:
    data = json.loads(body)
  except:
    pass
  data['params'] = dict(request.GET)
  data['headers'] = dict(request.headers)
  data['content_type'] = request.content_type
  return JsonResponse(data)