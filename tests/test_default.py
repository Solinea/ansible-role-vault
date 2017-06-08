import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
     '.molecule/ansible_inventory').get_hosts('all')


def test_vault_running_and_enabled(host):
    vault = host.service("vault")
    assert vault.is_running
    assert vault.is_enabled
