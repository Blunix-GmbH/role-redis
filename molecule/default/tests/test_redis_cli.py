import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_password_auth_enabled(host):
    r = host.run('echo "config get requirepass" | redis-cli -h 127.0.0.1 -p 6379 -a veryveryveryveryverysecret | grep requirepass')
    assert 'requirepass\n' == r.stdout
