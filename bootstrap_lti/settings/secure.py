'''
THIS FILE IS AN EXAMPLE ONLY!
None of the settings in this file will work out of the box
You should include this file in your .gitignore
'''
SECURE_SETTINGS = {
	'django_db_user': 'changeme',
	'django_db_pass': 'changeme',
	'django_secret_key': 'changeme,',
	'lti_oauth_credentials': {
		'key': 'value',
	},
	'admins': (
		('Admin User', 'admin_user@example.com'),
	),
	'canvas_token' : 'changeme',
}