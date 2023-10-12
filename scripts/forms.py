from wtforms import Form, StringField, IntegerField, validators

class buildinterface_form(Form):
    interface_name = StringField('Interface Name', [validators.InputRequired()])
    description = StringField('Description')
    vlan = IntegerField('VLAN', [validators.InputRequired()])
    ip_address = StringField('IP Address', [validators.InputRequired()])

class buildmsb_form(Form):
    host_name = StringField('Host Name', [validators.InputRequired()])
    domain_name = StringField('Domain Name', [validators.InputRequired()])
    ntp_01 = StringField('NTP 01', [validators.InputRequired()])  
    ntp_02 = StringField('NTP 02', [validators.InputRequired()]) 
    management_ip = StringField('Management IP', [validators.InputRequired()])  