from datetime import date
import random

from fabric.api import *
from fabric.utils import warn
from fabric.contrib import *
from fabric.contrib.project import rsync_project

from confighelper import ConfigHelper

@task
def setup(enviro='dev'):
	# init'ing empty string for hosts here, since we are populating it here
	ch = ConfigHelper('./config.json', '')
	conf = ch.get_conf('env_map')
	env.hosts = [conf[enviro]]
	env.user = 'tinisi'

@task
def deploy(enviro='dev'):
	# hoover up some config
	ch = ConfigHelper('./config.json', env.host)
	conf = ch.get_host_conf(enviro)
	local_dir = conf['source_path']
	remote_dir = conf['deploy_path']

	# verify no local changes for prod deployment only
	changes = None
	if enviro == 'prod':
		with lcd('../'):
			changes = local('git diff-index HEAD --', capture=True)
		if changes:
			abort('There are local changes in {}'.format(local_dir))

	# and finally we're ready to sync up the webroot
	rsync_project(
		local_dir=local_dir,
		remote_dir=remote_dir,
		delete=True,
		exclude=['.git','moonbase/podcast.php','.DS_Store']
	)

