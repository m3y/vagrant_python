# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://vagrantcloud.com/ubuntu/boxes/trusty64"

  config.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true

  config.ssh.forward_agent = true

  config.vm.provider "virtualbox" do |v|
      v.name = "vagrant_python"
      v.memory = 1024
  end

  config.vm.provision :fabric do |fabric|
      fabric.fabfile_path = "./fabfile.py"
      fabric.tasks = ["setup"]
  end
end
