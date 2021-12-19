# -*- coding: utf-8 -*-

# Copyright: (c) 2017, Ansible, Inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


class ModuleDocFragment(object):

    # Standard documentation fragment
    DOCUMENTATION = r'''
options:
    connection_type:
        description:
            - Type of connection to Zabbix API.
            - C(auto) will use C(zabbix-api) pip package for now but
              C(httpapi) is supposed to replace pip package over time.
            - Manual change to C(zabbix-api) ensure compatibility.
            - Manual change to C(httpapi) is experimental for now.
            - C(zabbix-api) or C(auto) will require C(server_url), C(login_user), C(login_password)
        required: false
        type: str
        default: 'auto'
        choices: ['auto','httpapi','zabbix-api']
    server_url:
        description:
            - URL of Zabbix server, with protocol (http or https).
              C(url) is an alias for C(server_url).
            - If not set the environment variable C(ZABBIX_SERVER) will be used.
            - Required if I(connection_type!=httpapi).
        required: false
        type: str
        aliases: [ url ]
    login_user:
        description:
            - Zabbix user name.
            - If not set the environment variable C(ZABBIX_USERNAME) will be used.
            - Required if I(connection_type!=httpapi).
        type: str
        required: false
    login_password:
        description:
            - Zabbix user password.
            - If not set the environment variable C(ZABBIX_PASSWORD) will be used.
            - Required if I(connection_type!=httpapi).
        type: str
        required: false
    http_login_user:
        description:
            - Basic Auth login
        type: str
    http_login_password:
        description:
            - Basic Auth password
        type: str
    timeout:
        description:
            - The timeout of API request (seconds).
        type: int
        default: 10
    validate_certs:
      description:
       - If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
       - If not set the environment variable C(ZABBIX_VALIDATE_CERTS) will be used.
      type: bool
      default: true
notes:
    - If you use I(login_password=zabbix), the word "zabbix" is replaced by "********" in all module output, because I(login_password) uses C(no_log).
      See L(this FAQ,https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.
'''
