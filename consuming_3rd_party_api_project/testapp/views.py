from django.shortcuts import render
import requests
# Create your views here.
def get_geographic_info(request):
    ip=request.META.get('HTTP_X_FORWARDED_FOR',"") or request.META.get('REMOTE_ADDR')
    url='http://api.ipstack.com/'+str(ip)+'?access_key=989ddbf4ddb06aa7654df341b69a8a62'
    response=requests.get(url)
    data=response.json()
    return render(request,'testapp/info.html',data)
