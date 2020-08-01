import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource(id=None):
    data={}
    if id is not None:
        data={'id':id}
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
get_resource(1)
''''
def get_all():
    resp=requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())
'''
'''
def create_resources():
    new_emp={
        'eno':500,
        'ename':'shiva',
        'esal':50000,
        'eaddr':'chennai',
    }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    #print(r.text)
    print(resp.json())
create_resources()

def update_resources(id):
    new_emp={
        'id':id,
        'eno':77777,
        'ename':'Karenna',
        'eaddr':'Lanka',
        'esal':15000,
    }
    resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
def delete_resource(id):
    data={
        'id':id,
    }
    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
delete_resource(1)
'''
'''
#same above using serialization
def get(self,request,id,*args,**kwargs):
    emp=Employee.objects.get(id=id)
    json_data=serialize('json',[emp,],fields=('eno','ename'))
    return HttpResponse(json_data,content_type='application/json')
'''