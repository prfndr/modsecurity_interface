# modsecurity_interface

В качестве парсера логов было использовано следующее решение:
https://github.com/molu8bits/modsecurity-parser

Инструкция по установке веб-интерфейса для ModSecurity:

# Необходимо внимательно сверять все пути для корректной установки.
Данная работа выполняется на ОС Ubuntu 22.04.
1)	Сперва, установите и настройте удобным для Вас образом ModSecurity 3.0.9 + Nginx 1.24.0.
2)	Затем, скачайте правила OWASP CRS 3.3.4.
3)	Для того, чтобы подключить правила OWASP CRS нужным образом, необходимо ввести в консоль следующую команду:
echo -e "Include owasp-crs/crs-setup.conf
Include owasp-crs/rules/REQUEST-901-INITIALIZATION.conf
Include owasp-crs/rules/REQUEST-903.9001-DRUPAL-EXCLUSION-RULES.conf
Include owasp-crs/rules/REQUEST-903.9002-WORDPRESS-EXCLUSION-RULES.conf
Include owasp-crs/rules/REQUEST-903.9003-NEXTCLOUD-EXCLUSION-RULES.conf
Include owasp-crs/rules/REQUEST-903.9004-DOKUWIKI-EXCLUSION-RULES.conf
Include owasp-crs/rules/REQUEST-903.9005-CPANEL-EXCLUSION-RULES.conf
Include owasp-crs/rules/REQUEST-903.9006-XENFORO-EXCLUSION-RULES.conf
Include owasp-crs/rules/REQUEST-905-COMMON-EXCEPTIONS.conf
Include owasp-crs/rules/REQUEST-910-IP-REPUTATION.conf
Include owasp-crs/rules/REQUEST-911-METHOD-ENFORCEMENT.conf
Include owasp-crs/rules/REQUEST-912-DOS-PROTECTION.conf
Include owasp-crs/rules/REQUEST-913-SCANNER-DETECTION.conf
Include owasp-crs/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf
Include owasp-crs/rules/REQUEST-921-PROTOCOL-ATTACK.conf
Include owasp-crs/rules/REQUEST-930-APPLICATION-ATTACK-LFI.conf
Include owasp-crs/rules/REQUEST-931-APPLICATION-ATTACK-RFI.conf
Include owasp-crs/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf
Include owasp-crs/rules/REQUEST-933-APPLICATION-ATTACK-PHP.conf
Include owasp-crs/rules/REQUEST-934-APPLICATION-ATTACK-NODEJS.conf
Include owasp-crs/rules/REQUEST-941-APPLICATION-ATTACK-XSS.conf
Include owasp-crs/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf
Include owasp-crs/rules/REQUEST-943-APPLICATION-ATTACK-SESSION-FIXATION.conf
Include owasp-crs/rules/REQUEST-944-APPLICATION-ATTACK-JAVA.conf
Include owasp-crs/rules/REQUEST-949-BLOCKING-EVALUATION.conf
Include owasp-crs/rules/RESPONSE-950-DATA-LEAKAGES.conf
Include owasp-crs/rules/RESPONSE-951-DATA-LEAKAGES-SQL.conf
Include owasp-crs/rules/RESPONSE-952-DATA-LEAKAGES-JAVA.conf
Include owasp-crs/rules/RESPONSE-953-DATA-LEAKAGES-PHP.conf
Include owasp-crs/rules/RESPONSE-954-DATA-LEAKAGES-IIS.conf
Include owasp-crs/rules/RESPONSE-959-BLOCKING-EVALUATION.conf
Include owasp-crs/rules/RESPONSE-980-CORRELATION.conf" >> /usr/local/nginx/conf/modsecurity.conf

4)	Далее установите Flask с помощью команды: 
sudo apt install -y python3-pip
sudo pip3 install flask

5)	Затем установите необходимые зависимости, указав путь к файлу requirements.txt в подпапке modsecurity-parser
sudo pip3 install -r ./requirements.txt

6)	Затем откройте файл app.py с помощью любого текстового редактора и пропишите корректные пути в самом начале к файлам и директориям:
-	modsec_conf_path  - путь к конфигурационному файлу ModSecurity,
-	owasp_conf_path  - путь к конфигурационному файлу OWASP CRS,
-	modsec_parser_path - путь к исполняемому файлу средства анализа журнала аудита ModSecurity,
-	modsec_output_path  - путь к директории с файлами анализа журнала аудита ModSecurity,
-	modsec_log_path - путь к журналу аудита ModSecurity.

7)	Затем сохраните и запустите интерфейс с помощью команды:
sudo python3 app.py
8)	Интерфейс будет доступен в браузере по адресу:
localhost:5000

-----------------------------

The following solution was used as a log parser:
https://github.com/molu8bits/modsecurity-parser

Instructions for installing the web interface for ModSecurity:

# It is necessary to carefully check all the paths for correct installation.
This work is performed on Ubuntu OS 22.04.
1) First, install and configure ModSecurity 3.0.9 + Nginx 1.24.0 in a way that is convenient for you.
2) Then download the OWASP CRS rules 3.3.4.
3) In order to connect the OWASP CRS rules in the right way, you need to enter the following command into the console:
echo -e "Include owasp-crs/crs-setup.conf
Include owasp-crs/rules/REQUEST-901-INITIALIZATION.conf
Include owasp-crs/rules/REQUEST-903.9001-DRUPAL-EXCLUSION-RULES.conf
Include owasp-crs/rules/REQUEST-903.9002-WORDPRESS-EXCLUSION-RULES.conf
Include owasp-crs/rules/REQUEST-903.9003-NEXTCLOUD-EXCLUSION-RULES.conf
Include owasp-crs/rules/REQUEST-903.9004-DOKUWIKI-EXCLUSION-RULES.conf
Include owasp-crs/rules/REQUEST-903.9005-CPANEL-EXCLUSION-RULES.conf
Include owasp-crs/rules/REQUEST-903.9006-XENFORO-EXCLUSION-RULES.conf
Include owasp-crs/rules/REQUEST-905-COMMON-EXCEPTIONS.conf
Include owasp-crs/rules/REQUEST-910-IP-REPUTATION.conf
Include owasp-crs/rules/REQUEST-911-METHOD-ENFORCEMENT.conf
Include owasp-crs/rules/REQUEST-912-DOS-PROTECTION.conf
Include owasp-crs/rules/REQUEST-913-SCANNER-DETECTION.conf
Include owasp-crs/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf
Include owasp-crs/rules/REQUEST-921-PROTOCOL-ATTACK.conf
Include owasp-crs/rules/REQUEST-930-APPLICATION-ATTACK-LFI.conf
Include owasp-crs/rules/REQUEST-931-APPLICATION-ATTACK-RFI.conf
Include owasp-crs/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf
Include owasp-crs/rules/REQUEST-933-APPLICATION-ATTACK-PHP.conf
Include owasp-crs/rules/REQUEST-934-APPLICATION-ATTACK-NODEJS.conf
Include owasp-crs/rules/REQUEST-941-APPLICATION-ATTACK-XSS.conf
Include owasp-crs/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf
Include owasp-crs/rules/REQUEST-943-APPLICATION-ATTACK-SESSION-FIXATION.conf
Include owasp-crs/rules/REQUEST-944-APPLICATION-ATTACK-JAVA.conf
Include owasp-crs/rules/REQUEST-949-BLOCKING-EVALUATION.conf
Include owasp-crs/rules/RESPONSE-950-DATA-LEAKAGES.conf
Include owasp-crs/rules/RESPONSE-951-DATA-LEAKAGES-SQL.conf
Include owasp-crs/rules/RESPONSE-952-DATA-LEAKAGES-JAVA.conf
Include owasp-crs/rules/RESPONSE-953-DATA-LEAKAGES-PHP.conf
Include owasp-crs/rules/RESPONSE-954-DATA-LEAKAGES-IIS.conf
Include owasp-crs/rules/RESPONSE-959-BLOCKING-EVALUATION.conf
Include owasp-crs/rules/RESPONSE-980-CORRELATION.conf" >> /usr/local/nginx/conf/modsecurity.conf

4) Next, install Flask using the command:
sudo apt install -y python3-pip
sudo pip3 install flask

5) Then install the necessary dependencies by specifying the path to the file requirements.txt in the modsecurity-parser subfolder
sudo pip3 install -r ./requirements.txt

6) Then open the file app.py use any text editor and write down the correct paths at the very beginning to the files and directories:
- modsec_conf_path - path to the ModSecurity configuration file,
- owasp_conf_path - path to the OWASP CRS configuration file,
- modsec_parser_path - path to the executable file of the ModSecurity audit log analysis tool,
- modsec_output_path - path to the directory with the ModSecurity audit log analysis files,
- modsec_log_path - path to the ModSecurity audit log.

7) Then save and run the interface using the command:
sudo python3 app.py
8) The interface will be available in the browser at
: localhost:5000
