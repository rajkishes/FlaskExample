from jinja2 import Template


def build_interface(interface_name, description, vlan, ip_address):
    variables = {'interface_name':interface_name,
                'description':description,
                'vlan':vlan,
                'ip_address':ip_address}

    with open('./scripts/jinja_templates/interface.j2') as file:
        jinja_template = Template(file.read())
        config = jinja_template.render(variables=variables)
        return config

def build_msb(host_name, domain_name, ntp_01, ntp_02, management_ip):
    variables = {'host_name':host_name,
                'domain_name':domain_name,
                'ntp_01':ntp_01,
                'ntp_02':ntp_02,
                'management_ip':management_ip}

    with open('./scripts/jinja_templates/msb.j2') as file:
        jinja_template = Template(file.read())
        config = jinja_template.render(variables=variables)
        return config
