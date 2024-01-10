#!/usr/bin/env python3

import json
import subprocess

# Run Terraform output to get the JSON representation of the infrastructure
terraform_output = subprocess.run(["terraform", "output", "-json"], capture_output=True, text=True)
output_json = json.loads(terraform_output.stdout)

# Extract instance IP addresses or hostnames from the Terraform output
jenkins_controller_ip = output_json["jenkins_controller_ip"]["value"]
jenkins_agent_ips = output_json["jenkins_agent_ips"]["value"]

# Create a dynamic inventory dictionary
inventory = {
    "jenkins_controller": {
        "hosts": [jenkins_controller_ip],
    },
    "jenkins_agents": {
        "hosts": jenkins_agent_ips,
    },
    "_meta": {
        "hostvars": {},
    }
}

# Print the dynamic inventory as JSON
print(json.dumps(inventory))
