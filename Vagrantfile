# -*- mode: ruby -*-
# vi: set ft=ruby :
require 'yaml'
settings = YAML.load_file('vagrant.yml')

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define settings['vm_name']
  config.vm.box = settings['box_name']
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 443, host: 443
  config.vm.network "forwarded_port", guest: 8001, host: 8001

  config.vm.network :private_network, ip: settings['ip_address']
  config.vm.synced_folder "blog/", "/blog", owner: "vagrant", group: "vagrant"
  config.vm.host_name = settings['host_name']

  config.vm.network :forwarded_port, guest: 1021, host: 1021
  config.vm.synced_folder "blog/", "/blog", owner: "vagrant", group: "vagrant"


  config.vm.provider "virtualbox" do |v|
    v.cpus = 4
    v.memory = 4096
  end

  config.vm.provision "shell", path: "./ext/ansible.sh"

  config.vm.provision 'ansible' do |ansible|
    ansible.playbook = "ext/playbook-pelican.yml"
     # ansible.verbose = 'vvv'
     ## For debugging
     #ansible.start_at_task = 'system'
     #ansible.start_at_task = 'latest node'
     #ansible.start_at_task = 'grunt'
  end

  config.vm.provision 'ansible' do |ansible|
    ansible.playbook = "ext/playbook-docker.yml"
    # ansible.verbose = 'vvv'
    ## For debugging
    # ansible.start_at_task = 'system'
    # ansible.start_at_task = 'latest node'
    # ansible.start_at_task = 'grunt'
  end
end
