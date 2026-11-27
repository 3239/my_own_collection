# Ansible Collection - my_own_namespace.yandex_cloud_elk

# my_own_namespace.yandex_cloud_elk

Custom Ansible collection containing `my_own_module` and `use_my_module` role.

## Contents

- **Modules:**
  - `my_own_module` \u2014 creates a text file on the remote host
- **Roles:**
  - `use_my_module` \u2014 role that uses `my_own_module`

## Installation

```bash
ansible-galaxy collection install my_own_namespace.yandex_cloud_elk
```
# Usage

## Using the module directly

```yaml
- hosts: localhost
  tasks:
    - name: Create file
      my_own_namespace.yandex_cloud_elk.my_own_module:
        path: /tmp/test.txt
        content: "Hello!"
```

## Using the role

```yaml
- hosts: localhost
  roles:
    - role: my_own_namespace.yandex_cloud_elk.use_my_module
      file_path: /tmp/test.txt
      file_content: "Hello from role!"
```

# Module Parameters

| Parameter | Required | Type | Description |
| :--- | :--- | :--- | :--- |
| path | yes | str | Absolute path where the file should be created |
| content | yes | str | Content to write into the file |

# License

MIT-0

# Autor

Kristina Filimonova - Netology student