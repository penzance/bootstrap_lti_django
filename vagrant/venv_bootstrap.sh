#!/bin/bash
export HOME=/home/vagrant
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv -a /home/vagrant/bootstrap_lti_django -r /home/vagrant/bootstrap_lti_django/bootstrap_lti_django/requirements/local.txt bootstrap_lti_django
