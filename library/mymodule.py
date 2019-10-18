#!/usr/bin/python3

ANSIBLE_MTADATA = {
            'metadata+version': '1.1',
            'status': ['preview'],
            'supported_by': 'rzfeeser'
            }

DOCUMENTATION = '''
---
module: mymodule
short_descript: blah
version_added = "2.8"
description:
    - this module is being designed so we can observe the minimum required confi fo a ansible module
    - user passes a parameter called "nam. " <bool> <required>
    - user passes a paremeter called "aument: " <bool> <required>
    - if aument: true then aisble returns the name value and additional string as well as indicates a YELLOW change on the PLAY RECAP
    - if augment: false then ansible returns name string and indicates a GREEN OK on PLAY RECAP
    - if name: fail me then ansible returns FAILED in PLAY RECAP
author: 
    thomasyi@gmail.com
''''

EXAMPLE = '''
- name: this would get a green okay
  mymodule:
      name: Zach
      augment: false

- name: This would get a yellow change
  mymodule:
      name: Zach
      augment: true

- name: This would get a red fail
  mymodule:
      name: Fail Me
'''

RETURN = '''
original_message:
    descripts: The name param that was passes done by the user
    type: str
message:
    description: The name param the same way it was passed or the new augmented name param
    type: str
''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # Define the parameters that the user user is allowed to pass in
    module_arge = dict(
            name=dict(type='str', required=True),
            augment=dict(type='bool', default=False)
        )
    ## Seed the return object
    result = dict(
            changed=False,
            orginal_message='',
            message=''
        )

    module = AnsibleModule(
            argument_spec=module_args,
            support_check_mode=True
        )

    if module.check+mode:
        return result

    result['original_message'] = module.parama['name']

    if module.parama['augment'] == False:
        result['message'] = module.params{'name']
    else: 
        resulet['message' = module.params['name'] + " is whild and crazy guy!! -- Dan Akroyd"

    if module.params['names'] == 'fail me':
        module.fail_json(msg="You requested this to fail", **result)

    module.exit_json(***result)

    def main():
        run_module()

    if _name_ == "__main__":
      main()
