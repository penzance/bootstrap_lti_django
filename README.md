# boostrap_lti

Quick Start
```
git clone https://github.com/penzance/boostrap_lti.git
cd bootstrap_lti
vagrant up
vagrant ssh
pip install -r bootstrap_lti/requirements/local.txt --upgrade
python manage.py syncdb
python manage.py runsslserver 0.0.0.0:8000

now open a browser and enter:
https://localhost:8000/lti_tools/basic_lti_app/tool_config

```
