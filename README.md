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

       
