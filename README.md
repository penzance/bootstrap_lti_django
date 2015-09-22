# boostrap_lti

## Quick Start

### Getting Started with Penzance and VirtualBox
If you would like to use the virtual machine configured for the bootstrap_LIT application, will need to download both Vagrant (https://www.vagrantup.com/downloads.html) and VirtualBox (https://www.virtualbox.org/wiki/Downloads). The following instructions assume Vagrant and VirtualBox are installed.

### Downloading the Repository and Configuring Vagrant
```
git clone https://github.com/penzance/bootstrap_lti_django.git
cd bootstrap_lti_django
vagrant up
vagrant ssh
pip install -r bootstrap_lti_django/requirements/local.txt --upgrade

# note you should be in a virtual env called bootstrap_lti_django now
# if not run "workon bootstrap_lti_django"
```

![Vagrant Screenshot](/images/vagrant_ssh.png)

### Obtain Canvas Integration Token
You will need to obtain a Canvas Integration Token. For more information about using tokens see: https://canvas.instructure.com/doc/api/file.oauth.html

You may obtain a token from the Canvas settings page:

![Obtain API Key 1](/images/obtain_api_key.png)
![Obtain API Key 2](/images/obtain_api_key_2.png)

### Edit secure.py

You must edit `secure.py` before deploying your application. The file `secure.py.example` can be used as a template. You must change all of the default values. If you do not have a `django_secret_key`, you may use the following commands to obtain one:

```
cd ~/junk # Go to some safe directory to create a new project.
django-admin startproject django_scratch
grep SECRET_KEY django_scratch/django_scratch/settings.py # copy to old project
rm -R django_scratch
```
Remember the key and value you choose for `lti_oauth_credentials`; you will need this when installing the tool in Canvas.

secure.py.example
```
SECURE_SETTINGS = {
	# you only need to change the database settings
	# if your app needs to access a database
	# you would also need to configure the
	# database in base.py. These settings are
	# here just to show you that you can put secure 
	# settings in this file. 
	'django_db_user': 'changeme',
	'django_db_pass': 'changeme',

	# required for Django
	'django_secret_key': 'changeme,',

	# required for LTI
	'lti_oauth_credentials': {
		'key': 'value',
	},
	
	'admins': (
		('Admin User', 'admin_user@example.com'),
	),
	
	# You will need to update the base_api_url with the url 
	# of your canvas instance.
	'base_api_url' : 'https://path-to-your-canvas-instance/api',

	# You will need to obtain a Canvas Integration Token. See this url
    # for more info: https://canvas.instructure.com/doc/api/file.oauth.html
	'canvas_token' : 'changeme',
}
```

### Initialize project
```
python manage.py syncdb
# You need to decide if you would like to create a superuser
python manage.py collectstatic
python manage.py runsslserver --addrport 0.0.0.0:8000
```
Now open a browser and enter:
`https://localhost:8000/lti_tools/basic_lti_app/tool_config`
Your browser will likely block you from viewing this page. You must override this.
![Chrome Security Warning](/images/chrome_error.png)
Copy all the XML data; you will need this to install your tool in Canvas.

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
### Install tool on Canvas
Navigate to the settings page of the COURSE you would like to install the tool for. (Note that this settings page can be found on the left sidebar of the course page. This is different from the settings page found in the upper right toolbar.)
![Add tool to Canvas 1](/images/add_app_canvas.png)
Click the "Add New App" button.
You may choose any name for the tool. Consumer Key and Shared Secret must be the key and value you choose for `lti_oauth_credentials` in `secure.py`. Configuration type should be Paste XML. In the following text box, paste the XML that was generated at `https://localhost:8000/lti_tools/basic_lti_app/tool_config`
![Add tool to Canvas 2](/images/add_app_canvas_2.png)