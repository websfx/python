* urls.py中path(r'api/namespace',views.namespace)的格式为：path(r"url"，对应函数，参数，url别名)参数为键值对形式
* def test(request,参数)是可以加参数的 在urls.py中使用正则表达式,如果在urls.py使用了名字，则后端在使用时需要使用同样的名字(有命url)
* form action={% url "test" %}