#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module
short_description: Create a text file on the remote host
version_added: "1.0.0"
description:
    - This module creates a text file on the remote host at the specified path
      with the given content.
options:
    path:
        description: The absolute path where the file should be created.
        required: true
        type: str
    content:
        description: The content to write into the file.
        required: true
        type: str
author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a simple text file
  my_own_module:
    path: /tmp/test.txt
    content: "Hello from my module!"

- name: Create file with multiline content
  my_own_module:
    path: /tmp/notes.txt
    content: |
      Line 1
      Line 2
      Line 3
'''

RETURN = r'''
path:
    description: The path of the created file.
    type: str
    returned: always
    sample: '/tmp/test.txt'
content_length:
    description: The length of the written content.
    type: int
    returned: always
    sample: 21
'''

import os
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content_length=0
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    file_path = module.params['path']
    content = module.params['content']

    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            existing_content = f.read()
        if existing_content == content:
            result['path'] = file_path
            result['content_length'] = len(content)
            module.exit_json(**result)

    if module.check_mode:
        result['changed'] = True
        result['path'] = file_path
        result['content_length'] = len(content)
        module.exit_json(**result)

    try:
        with open(file_path, 'w') as f:
            f.write(content)
        result['changed'] = True
        result['path'] = file_path
        result['content_length'] = len(content)
    except Exception as e:
        module.fail_json(msg=f"Failed to create file: {str(e)}", **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()