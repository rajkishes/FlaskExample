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

