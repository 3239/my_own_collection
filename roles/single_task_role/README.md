Role Name
=========

Role that uses `my_own_module` from `my_own_namespace.yandex_cloud_elk` collection to create text files on remote hosts.

Requirements
------------

- Ansible 2.10+
- Collection `my_own_namespace.yandex_cloud_elk` installed

Role Variables
--------------

| Variable | Description | Default |
|----------|-------------|---------|
| `file_path` | Path where the file should be created | `/tmp/default_module_file.txt` |
| `file_content` | Content to write into the file | `Default content from role` |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: localhost
  roles:
    - role: my_own_namespace.yandex_cloud_elk.use_my_module
      file_path: /tmp/custom.txt
      file_content: "Custom content"

License
-------

MIT-0

Author Information
------------------

Kristina Filimonova - Netology student.

