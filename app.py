from flask import Flask, render_template, request
from jinja2 import Template
import subprocess, os

app = Flask(__name__)

modsec_conf_path = "/usr/local/nginx/conf/modsecurity.conf"
owasp_conf_path = "/usr/local/nginx/conf/owasp-crs/crs-setup.conf"
modsec_parser_path = "/usr/local/nginx/modsecurity-parser/modsecurity_parser.py"
modsec_output_path = "/var/log/modsec_output"
modsec_log_path = "/var/log/modsec_audit.log"

@app.route('/', methods=['GET','POST'])            
def modsec():
    if request.method == 'POST':
        action = request.form.get('action')
        SelectPL = request.form.get('SelectPL')
        if action == 'on':
            subprocess.call(["sudo", "sed", "-i",
                             "s/SecRuleEngine DetectionOnly/SecRuleEngine On/g",
                             modsec_conf_path])
            subprocess.call(["sudo", "systemctl", "restart", "nginx"])
        elif action == 'off':
            subprocess.call(["sudo", "sed", "-i",
                             "s/SecRuleEngine On/SecRuleEngine DetectionOnly/g",
                             modsec_conf_path])
            subprocess.call(["sudo", "systemctl", "restart", "nginx"])
        subprocess.call(["sudo", "sed", "-i",
                        "176,182 s/#//g",
                        owasp_conf_path])
        
        if SelectPL == 'PL1':
            subprocess.call(["sudo", "sed", "-i",
                            "182 s/[0-9]//g",
                            owasp_conf_path])
            subprocess.call(["sudo", "sed", "-i",
                            "182 s/setvar:tx.paranoia_level=/setvar:tx.paranoia_level=1/g",
                            owasp_conf_path])
            subprocess.call(["sudo", "systemctl", "restart", "nginx"])
        elif SelectPL == 'PL2':
            subprocess.call(["sudo", "sed", "-i",
                            "182 s/[0-9]//g",
                            owasp_conf_path])
            subprocess.call(["sudo", "sed", "-i",
                            "182 s/setvar:tx.paranoia_level=/setvar:tx.paranoia_level=2/g",
                            owasp_conf_path])
            subprocess.call(["sudo", "systemctl", "restart", "nginx"])
        elif SelectPL == 'PL3':
            subprocess.call(["sudo", "sed", "-i",
                            "182 s/[0-9]//g",
                            owasp_conf_path])
            subprocess.call(["sudo", "sed", "-i",
                            "182 s/setvar:tx.paranoia_level=/setvar:tx.paranoia_level=3/g",
                            owasp_conf_path])
            subprocess.call(["sudo", "systemctl", "restart", "nginx"])
        elif SelectPL == 'PL4':
            subprocess.call(["sudo", "sed", "-i",
                            "182 s/[0-9]//g",
                            owasp_conf_path])
            subprocess.call(["sudo", "sed", "-i",
                            "182 s/setvar:tx.paranoia_level=/setvar:tx.paranoia_level=4/g",
                            owasp_conf_path])
            subprocess.call(["sudo", "systemctl", "restart", "nginx"])

    with open(modsec_conf_path, 'r') as f:
        config_sec = f.read()
    if 'SecRuleEngine On' in config_sec:
        state = 'on'
    else:
        state = 'off'
    paranoia1_checked = ''
    paranoia2_checked = ''
    paranoia3_checked = ''
    paranoia4_checked = ''
    with open(owasp_conf_path, 'r') as a:
        config_owasp = a.read()
    if 'tx.paranoia_level=1' in config_owasp:
        paranoia1_checked = 'checked'
    elif 'tx.paranoia_level=2' in config_owasp:
        paranoia2_checked = 'checked'
    elif 'tx.paranoia_level=3' in config_owasp:
        paranoia3_checked = 'checked'
    elif 'tx.paranoia_level=4' in config_owasp:
        paranoia4_checked = 'checked'
    return render_template('index.html',
                           state=state,
                           paranoia1_checked=paranoia1_checked,
                           paranoia2_checked=paranoia2_checked,
                           paranoia3_checked=paranoia3_checked,
                           paranoia4_checked=paranoia4_checked)

@app.route('/groups', methods=['GET','POST']) 
def groups():
    if request.method == 'POST':
        group2 = request.form.get('REQUEST-910-IP-REPUTATION')
        group3 = request.form.get('REQUEST-911-METHOD-ENFORCEMENT')
        group4 = request.form.get('REQUEST-912-DOS-PROTECTION')
        group5 = request.form.get('REQUEST-913-SCANNER-DETECTION')
        group6 = request.form.get('REQUEST-920-PROTOCOL-ENFORCEMENT')
        group7 = request.form.get('REQUEST-921-PROTOCOL-ATTACK')
        group8 = request.form.get('REQUEST-930-APPLICATION-ATTACK-LFI')
        group9 = request.form.get('REQUEST-931-APPLICATION-ATTACK-RFI')
        group10 = request.form.get('REQUEST-932-APPLICATION-ATTACK-RCE')
        group11 = request.form.get('REQUEST-933-APPLICATION-ATTACK-PHP')
        group12 = request.form.get('REQUEST-934-APPLICATION-ATTACK-NODEJS')
        group13 = request.form.get('REQUEST-941-APPLICATION-ATTACK-XSS')
        group14 = request.form.get('REQUEST-942-APPLICATION-ATTACK-SQLI')
        group15 = request.form.get('REQUEST-943-APPLICATION-ATTACK-SESSION-FIXATION')
        group16 = request.form.get('REQUEST-944-APPLICATION-ATTACK-JAVA')

        if group2:
            subprocess.call(["sudo", "sed", "-i", "295 s/#//g", modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "295 s/Include/#Include/g", modsec_conf_path])
        if group3:
            subprocess.call(["sudo", "sed", "-i", "296 s/#//g", modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "296 s/Include/#Include/g", modsec_conf_path])
        if group4:
            subprocess.call(["sudo", "sed", "-i", "297 s/#//g", modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "297 s/Include/#Include/g", modsec_conf_path])
        if group5:
            subprocess.call(["sudo", "sed", "-i", "298 s/#//g", modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "298 s/Include/#Include/g", modsec_conf_path])
        if group6:
            subprocess.call(["sudo", "sed", "-i", "299 s/#//g", modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "299 s/Include/#Include/g", modsec_conf_path])
        if group7:
            subprocess.call(["sudo", "sed", "-i", "300 s/#//g",modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "300 s/Include/#Include/g", modsec_conf_path])
        if group8:
            subprocess.call(["sudo", "sed", "-i", "301 s/#//g", modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "301 s/Include/#Include/g", modsec_conf_path])
        if group9:
            subprocess.call(["sudo", "sed", "-i", "302 s/#//g", modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "302 s/Include/#Include/g", modsec_conf_path])
        if group10:
            subprocess.call(["sudo", "sed", "-i", "303 s/#//g", modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "303 s/Include/#Include/g", modsec_conf_path])
        if group11:
            subprocess.call(["sudo", "sed", "-i", "304 s/#//g", modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "304 s/Include/#Include/g", modsec_conf_path])
        if group12:
            subprocess.call(["sudo", "sed", "-i", "305 s/#//g", modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "305 s/Include/#Include/g", modsec_conf_path])
        if group13:
            subprocess.call(["sudo", "sed", "-i", "306 s/#//g", modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "306 s/Include/#Include/g", modsec_conf_path])
        if group14:
            subprocess.call(["sudo", "sed", "-i", "307 s/#//g", modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "307 s/Include/#Include/g", modsec_conf_path])
        if group15:
            subprocess.call(["sudo", "sed", "-i", "308 s/#//g", modsec_conf_path])
        else: 
            subprocess.call(["sudo", "sed", "-i", "308 s/Include/#Include/g", modsec_conf_path])
        if group16:
            subprocess.call(["sudo", "sed", "-i", "309 s/#//g", modsec_conf_path])
            subprocess.call(["sudo", "systemctl", "restart", "nginx"])
        else: 
            subprocess.call(["sudo", "sed", "-i", "309 s/Include/#Include/g", modsec_conf_path])
            subprocess.call(["sudo", "systemctl", "restart", "nginx"])

    with open(modsec_conf_path, 'r') as file:
        lines = file.readlines()
        group2_checked = 'checked'
        group3_checked = 'checked'
        group4_checked = 'checked'
        group5_checked = 'checked'
        group6_checked = 'checked'
        group7_checked = 'checked'
        group8_checked = 'checked'
        group9_checked = 'checked'
        group10_checked = 'checked'
        group11_checked = 'checked'
        group12_checked = 'checked'
        group13_checked = 'checked'
        group14_checked = 'checked'
        group15_checked = 'checked'
        group16_checked = 'checked'
        for line in lines:
            if '#Include owasp-crs/rules/REQUEST-910-IP-REPUTATION.conf' in line:
                group2_checked = ''
            if '#Include owasp-crs/rules/REQUEST-911-METHOD-ENFORCEMENT.conf' in line:
                group3_checked = ''
            if '#Include owasp-crs/rules/REQUEST-912-DOS-PROTECTION.conf' in line:
                group4_checked = ''
            if '#Include owasp-crs/rules/REQUEST-913-SCANNER-DETECTION.conf' in line:
                group5_checked = ''
            if '#Include owasp-crs/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf' in line:
                group6_checked = ''
            if '#Include owasp-crs/rules/REQUEST-921-PROTOCOL-ATTACK.conf' in line:
                group7_checked = ''
            if '#Include owasp-crs/rules/REQUEST-930-APPLICATION-ATTACK-LFI.conf' in line:
                group8_checked = ''
            if '#Include owasp-crs/rules/REQUEST-931-APPLICATION-ATTACK-RFI.conf' in line:
                group9_checked = ''
            if '#Include owasp-crs/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf' in line:
                group10_checked = ''
            if '#Include owasp-crs/rules/REQUEST-933-APPLICATION-ATTACK-PHP.conf' in line:
                group11_checked = ''
            if '#Include owasp-crs/rules/REQUEST-934-APPLICATION-ATTACK-NODEJS.conf' in line:
                group12_checked = ''
            if '#Include owasp-crs/rules/REQUEST-941-APPLICATION-ATTACK-XSS.conf' in line:
                group13_checked = ''
            if '#Include owasp-crs/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf' in line:
                group14_checked = ''
            if '#Include owasp-crs/rules/REQUEST-943-APPLICATION-ATTACK-SESSION-FIXATION.conf' in line:
                group15_checked = ''
            if '#Include owasp-crs/rules/REQUEST-944-APPLICATION-ATTACK-JAVA.conf' in line:
                group16_checked = ''

    return render_template('groups.html',
                            group2_checked=group2_checked,
                            group3_checked=group3_checked,
                            group4_checked=group4_checked,
                            group5_checked=group5_checked,
                            group6_checked=group6_checked,
                            group7_checked=group7_checked,
                            group8_checked=group8_checked,
                            group9_checked=group9_checked,
                            group10_checked=group10_checked,
                            group11_checked=group11_checked,
                            group12_checked=group12_checked,
                            group13_checked=group13_checked,
                            group14_checked=group14_checked,
                            group15_checked=group15_checked,
                            group16_checked=group16_checked)

@app.route('/parser', methods=['GET','POST']) 
def parser():
    pars = request.form.get("pars")
    show = request.form.get("show")
    if pars == 'Analysis':
        subprocess.call(["sudo",
                         "python3",
                         modsec_parser_path,
                         "-f", modsec_log_path, "--version3"])
    if show == 'Show':
        files = os.listdir(modsec_output_path)
        if files:
            files = [os.path.join(modsec_output_path, file) for file in files]
            files = [file for file in files if os.path.isfile(file) and file.endswith(".xlsx")]
            xlsx = (max(files, key=os.path.getctime))
            subprocess.call(["sudo", "libreoffice", "--calc", xlsx])
    return render_template('parser.html')

if __name__ == '__main__':
    app.run(port=5000)

