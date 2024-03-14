import ansible_runner

r = ansible_runner.run(private_data_dir=".", playbook='./hello.yml', inventory='./hosts.yml',)