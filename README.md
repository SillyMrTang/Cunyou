# 基于django-rest-framework 提供后台接口，以及xadmin进行后台管理
## 这里只是做一些简单的说明，详情请查看 https://cloud.tencent.com/developer/article/1005607
     
#### 创建django 项目， 修改settings.py配置。相信大家都比较熟悉，我就不再重复了。直接步入正题       
>创建好项目以后导入xadmin，可下载源码放置项目根目录与static同级 https://github.com/sshwsfc/xadmin        
修改settings.py       
```
NSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',#添加
    'crispy_forms',#添加
]

```       
国际化设置          
```
 LANGUAGE_CODE = 'zh-hans'#更改(xadmin中文)

  TIME_ZONE = 'Asia/Shanghai'#更改
```       
修改主路由          
```
url('xadmin/', xadmin.site.urls),
```            
然后新建一个adminx.py进行xadmin的配置         
```
from xadmin import views
from .models import TypeModel, TypeContent
import xadmin


class TypeAdmin(object):
    list_display = ['id', 'name', 'image', 'create_time']
    search_fields = ['name', ]
    ordering = ('id',)


class ContentAdmin(object):
    list_display = ['id', 'name', 'image', 'path', 'type']
    search_fields = ['name', ]
    ordering = ('id',)


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True  # 支持切换主题


class GlobalSettings(object):
    """修改后台标题"""
    site_title = "村游六品后台管理"


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(TypeModel, TypeAdmin)
xadmin.site.register(TypeContent, ContentAdmin)
```            
### xamdin的基本配置完成，可创建超级用户运行项目进行查看，接下来开始创建一哥vue前端项目          
>使用npm安装vue-cli脚手架工具,如果环境中没有npm的老铁，请进行node的环境配置        
```
npm install -g vue-cli
```       
>安装好后再所在的django项目根目录下新建一个前端工程目录         
```
vue-init webpack vue-project
```       
> 进入vue-project目录，运行          
```
npm install // 安装vue所需的node依赖
```       
前端项目创建完毕，可以写前端代码咯，不过在写前端代码的时候关于跨域请求的问题要注意了，如下图：        
![https://blog-10039692.file.myqcloud.com/1501640848145_4871_1501640848404.jpg](https://blog-10039692.file.myqcloud.com/1501640848145_4871_1501640848404.jpg)        
这时候我们须要在Django层注入header，用Django的第三方包django-cors-headers来解决跨域问题：       
```
pip install django-cors-headers
```
settings.py修改配置,注意中间件位置          
```
INSTALLED_APPS = [
    ...
    'crispy_forms',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True
```       
解决跨域请求就可以在前端目录vue-project输入npm run dev 运行         
然后运行npm run build 对vue进行webpack打包处理


###  整合Django + Vue.js
>配置url，访问/直接返回vue的index.html       

```
urlpatterns = [
    ...
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
```       
>修改setting.py下的TEMPLATES      
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['vue-project/dist'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```      
>配置静态文件static       
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "vue-project/dist/static"),
]
```
>配置完成，可以运行django项目，查看效果
### 部署到服务器
我使用的是nignx + uwsgi 进行部署，这里不贴代码。有问题可咨询wx:onlylovejing08

       
