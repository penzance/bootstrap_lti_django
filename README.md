# boostrap_lti

Quick Start
```
git clone https://github.com/penzance/bootstrap_lti.git
cd bootstrap_lti
vagrant up
vagrant ssh
pip install -r bootstrap_lti/requirements/local.txt --upgrade

# note you should be in a virtual env called bootstrap_lti now
# if not run "workon bootstrap_lti"

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
	'canvas_token' : 'your-Canvas-Integration-Token', # add your canvas token here
}
```

In base.py you will need to add or edit the following section. You will need to update the 
base_api_url with the url of your canvas instance. 

base.py
```

CANVAS_SDK_SETTINGS = {
    'auth_token': SECURE_SETTINGS.get('canvas_token', None),
    'base_api_url': 'https://your-canvas-domain-name-here/api', # you need to add your own canvas domain here
    'max_retries': 3,
    'per_page': 40,
}
```

```
python manage.py syncdb
python manage.py runsslserver 0.0.0.0:8000

now open a browser and enter:
https://localhost:8000/lti_tools/basic_lti_app/tool_config

You can use the XML from the url above to install the tool into your LMS.

```
