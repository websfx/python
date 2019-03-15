* request response
* request中方法：GET POST  path COOKIES files
* render(建议使用) render_to_response
* locals()使用本地变量
* redirect 登录验证时，用redirect更好
* templates
* render(request,"index.html",{"data": user_list}) index.html叫模本 {"data": user_list}叫上下文,引入template context
* python manage.py shell
* {{变量}} 万能的句点号:. {% if %} {% endif %} {% for %} {% endfor %}{forloop.counter}
* filter:{{ obj|upper }} {{ obj|lower }} {{ obj|first|upper }} {{ obj|capfirst }}
* {{ obj|add:1 }} {{ obj|date: 'Y-m-d' }}  {{ obj|urlencode }}