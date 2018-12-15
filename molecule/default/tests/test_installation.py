"""
Role tests
"""

import os
import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# Docker
# -----------------------------------------------------------------------------
def test_docker_package(host):
    """
    Ensure "docker-ce" package installed
    """

    assert host.package('docker-ce').is_installed


def test_docker_group(host):
    """
    Ensure "docker" group exists
    """

    assert host.group('docker').exists


def test_docker_service(host):
    """
    Ensure "docker" service running and enabled
    """

    assert host.service('docker').is_enabled
    assert host.service('docker').is_running


def test_docker_compose_bin(host):
    """
    Ensure "docker-compose" installed
    """

    docker_compose_file_path = '/usr/local/bin/docker-compose'

    assert host.file(docker_compose_file_path).exists
    assert host.file(docker_compose_file_path).is_file
    assert host.file(docker_compose_file_path).user == 'root'
    assert host.file(docker_compose_file_path).group == 'root'
    assert host.file(docker_compose_file_path).mode == 0o0755


def test_docker_pip_package(host):
    """
    Ensure "docker" pip package installed
    """

    assert 'docker' in host.pip_package.get_packages()


# Service
# -----------------------------------------------------------------------------
@pytest.mark.parametrize('path,user,group,mode', [
    ('/opt/infopen', 'root', 'root', 0o755),
    ('/opt/infopen/fake-service', 'root', 'root', 0o755),
    ('/opt/infopen/fake-service/releases', 'root', 'root', 0o755),
    ('/opt/infopen/fake-service/repo', 'root', 'root', 0o755),
    ('/opt/infopen/fake-service/shared', 'root', 'root', 0o755),
    ('/var/opt/infopen', 'root', 'root', 0o755),
    ('/var/opt/infopen/fake-service', 'root', 'root', 0o755),
])
def test_service_folders(host, path, user, group, mode):
    """
    Ensure service root folders exists and have expected permissions
    """

    current_folder = host.file(path)

    assert current_folder.exists
    assert current_folder.is_directory
    assert current_folder.user == user
    assert current_folder.group == group
    assert current_folder.mode == mode


def test_service_ansistrano_current_link(host):
    """
    Ensure service has a "current" symlink
    """

    symlink_path = host.file('/opt/infopen/fake-service/current')
    expected_symlink_to = '/opt/infopen/fake-service/releases/19700101-1.0.0'

    assert symlink_path.exists
    assert symlink_path.is_symlink
    assert symlink_path.linked_to == expected_symlink_to
    assert symlink_path.user == 'root'
    assert symlink_path.group == 'root'
