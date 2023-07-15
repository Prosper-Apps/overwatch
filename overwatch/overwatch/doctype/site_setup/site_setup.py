# Copyright (c) 2023, Flexcom Systems and contributors
# For license information, please see license.txt

import json
import frappe
from frappe import _
import requests
import subprocess

from frappe.model.document import Document

class SiteSetup(Document):
    pass



@frappe.whitelist(allow_guest=True)
def create_site(site_name, db_root_password, admin_password):
    print('function triggered')
    print( site_name, db_root_password, admin_password)
    
    # specify the full path of the playbook and inventory files
    playbook_path = "/home/flexy/frappe-bench/apps/overwatch/ansible/playbooks/create_site.yml"
    inventory_path = "/home/flexy/frappe-bench/apps/overwatch/ansible/inventories/production.ini"
    
    command = f"ansible-playbook -i {inventory_path} {playbook_path} --extra-vars \"site_name={site_name} db_root_password={db_root_password} admin_password={admin_password}\""

    try:
        # increase timeout limit to 1800 seconds (30 minutes)
        process = subprocess.run(command, shell=True, check=True, text=True, capture_output=True, timeout=1800)
    except subprocess.TimeoutExpired:
        return {'status': 'error', 'message': 'Command timed out'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': f'Command failed with exit code {e.returncode}: {e.output}'}

    return {'status': 'success', 'message': process.stdout}



@frappe.whitelist()
def install_app(agent_url, app_name):
    frappe.log_error("install_app function has been called", "Debug")
    url = f"{agent_url}/api/method/agent.api.requests.install_app"
    data = {'app_name': app_name}
    response = requests.post(url, json=data)
    return response.json()
