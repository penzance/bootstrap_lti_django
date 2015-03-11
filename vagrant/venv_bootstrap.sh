#!/bin/bash
export HOME=/home/vagrant
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv -a /home/vagrant/bootstrap_lti -r /home/vagrant/bootstrap_lti/bootstrap_lti/requirements/local.txt bootstrap_lti
