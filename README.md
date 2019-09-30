# docker-service

Common steps for docker services deployments

## Requirements

This role requires Ansible 2.5 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- CentOS 7
- Debian Stretch
- Ubuntu Bionic

and use:
- Ansible 2.5.x
- Ansible 2.6.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
# Ansistrano default settings
_ansistrano_deploy_to: "/opt/infopen/{{ _docker_service_project_name | mandatory }}"
_ansistrano_deploy_via: 'git'
ansistrano_after_update_code_tasks_file: "{{ _roles_path | default(playbook_dir ~ '/roles/externals') }}/{{ _docker_service_role_full_name | mandatory }}/tasks/after_update_code.yml"
ansistrano_after_cleanup_tasks_file: "{{ _roles_path | default(playbook_dir ~ '/roles/externals') }}/{{ _docker_service_role_full_name | mandatory }}/tasks/after_clean_up.yml"


# Docker registries credentials
_docker_registries: []


# Docker override
_docker_service_compose_override: {}


# Manage docker prerequisites and external items
_docker_service_ansistrano_role_name: 'ansistrano.deploy__3.2.0'
_docker_service_compose_options: ''
_docker_service_compose_path: '/usr/local/bin/docker-compose'
_docker_service_files: []
_docker_service_folders:
  - path: '/opt/infopen'
  - path: "/opt/infopen/{{ _docker_service_project_name }}"
  - path: '/var/opt/infopen'
  - path: "/var/opt/infopen/{{ _docker_service_project_name }}"
_docker_service_networks:
  - name: 'services'
_docker_service_templates: []
_docker_service_volumes: []
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infopen.docker-service }
```

## License

''

## Author Information

Alexandre Chaussier (for Infopen company)
- https://infopen.pro
- alexandre.chaussier [at] infopen.pro
