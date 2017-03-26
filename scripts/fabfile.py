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
	backup_path = conf['backup_path']

	# verify no local changes for prod deployment only
	changes = None
	if enviro == 'prod':
		with lcd('../'):
			changes = local('git diff-index HEAD --', capture=True)
		if changes:
			abort('There are local changes in {}'.format(local_dir))

	# backup, wipe and reset data file for php script in contact_us/index.php
	data_source='/contact_us/contact_log.txt'
	data_file_path = '{remote_dir}{data_source}'.format(remote_dir=remote_dir, data_source=data_source)
	if files.exists(data_file_path):
		date_stamp = date.today().strftime("%Y%m%d_{rand}".format(rand=random.randint(100,990)))
		# make a backup
		run('cp {data_file_path} {backup_path}/contact_log_{date_stamp}.txt'.format(data_file_path=data_file_path, backup_path=backup_path, date_stamp=date_stamp))
		# wipe and reset data file
		run('rm {data_file_path}'.format(data_file_path=data_file_path))
		run('touch {data_file_path} && chmod o=wr {data_file_path}'.format(data_file_path=data_file_path))

	# and finally we're ready to sync up the webroot
	rsync_project(
		local_dir=local_dir,
		remote_dir=remote_dir,
		delete=True,
		exclude=['.git','contact_us/contact_log.txt','.DS_Store']
	)

