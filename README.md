# boostrap_lti

Quick Start
```
git clone https://github.com/penzance/bootstrap_lti_django.git
cd bootstrap_lti_django
vagrant up
vagrant ssh
pip install -r bootstrap_lti_django/requirements/local.txt --upgrade

# note you should be in a virtual env called bootstrap_lti_django now
# if not run "workon bootstrap_lti_django"

```
You will need to obtain a Canvas Integration Token. See this url
for more info: https://canvas.instructure.com/doc/api/file.oauth.html

Once you have your token, you will need to add the token to the secure.py file and 
edit the base.py file in the settings folder.

secure.py
```
SECURE_SETTINGS = {
	'django_db_user': 'changeme',
	'django_db_pass': 'changeme',
	'django_secret_key': 'your-django-secret-key', 
	'lti_oauth_credentials': {
		'test': 'test', # you will not want to use these values for production
	},
	'admins': (
		('Admin User', 'admin_user@example.com'),
	),

	# You will need to update the base_api_url with the url 
	# of your canvas instance. 
	'base_api_url' : 'https://your-canvas-domain-name-here/api',

	# add your canvas token here
	'canvas_token' : 'your-Canvas-Integration-Token', 
}
```

In base.py you will need to add or edit the following section. 

base.py
```

CANVAS_SDK_SETTINGS = {
    'auth_token': SECURE_SETTINGS.get('canvas_token'),
    'base_api_url': SECURE_SETTINGS.get('base_api_url'),
    'max_retries': 3,
    'per_page': 40,
}
```

```
python manage.py syncdb
python manage.py collectstatic
python manage.py runsslserver --addrport 0.0.0.0:8000

now open a browser and enter:
https://localhost:8000/lti_tools/basic_lti_app/tool_config

You can use the XML from the url above to install the tool into your LMS.

```

Tool Config XML Example
```
<?xml version="1.0" encoding="UTF-8"?>
<cartridge_basiclti_link 
	xmlns:lticm="http://www.imsglobal.org/xsd/imslticm_v1p0" 
	xmlns:blti="http://www.imsglobal.org/xsd/imsbasiclti_v1p0" 
	xmlns:lticp="http://www.imsglobal.org/xsd/imslticp_v1p0" 
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
	xmlns="http://www.imsglobal.org/xsd/imslticc_v1p0" 
	xsi:schemaLocation="http://www.imsglobal.org/xsd/imslticc_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticc_v1p0.xsd http://www.imsglobal.org/xsd/imsbasiclti_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imsbasiclti_v1p0p1.xsd http://www.imsglobal.org/xsd/imslticm_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticm_v1p0.xsd http://www.imsglobal.org/xsd/imslticp_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticp_v1p0.xsd">
	<blti:title>Basic LTI App</blti:title>
	<blti:description>This LTI app shows all the LTI parameters</blti:description>
	<blti:launch_url>https://localhost:8000/lti_tools/basic_lti_app/lti_launch</blti:launch_url>
	<blti:secure_launch_url>https://localhost:8000/lti_tools/basic_lti_app/lti_launch</blti:secure_launch_url>
	<blti:vendor/>
	<blti:extensions platform="canvas.instructure.com">
		<lticm:property name="privacy_level">public</lticm:property>
		<lticm:options name="course_navigation">
			<lticm:property name="text">basic lti app</lticm:property>
			<lticm:property name="enabled">true</lticm:property>
		</lticm:options>
	</blti:extensions>
</cartridge_basiclti_link>
```
