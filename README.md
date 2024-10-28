# Network Templater

```
git pull git@github.com:yury-nazarov/network_templater.git
```

или скачать содержимое репозитория к себе на ПК

зайти в директорию со скриптом
```
cd network_templater
```

В директорию `networks` складываешь файлы в формате

```
vpn_list
Network ISP-01
192.168.100.0/24
192.168.200.0/24
192.168.300.0/24
```

где 
1. `vpn_list` - нужный тебе `list`
2. `Network ISP-01` - comment
3. Список сетей в нужном кол-во

Добавить права на выполнение файла
```bash
 chmod +x templater.py
```
Запускаешь
```bash
python templater.py
```

в терминале появится 
```bash
/ip firewall address-list
add list=vpn_list comment="Network ISP-03" address=172.16.1.0/24
add list=vpn_list comment="Network ISP-03" address=172.16.2.0/24
add list=vpn_list comment="Network ISP-03" address=172.16.3.0/24
add list=vpn_list comment="Network ISP-02" address=10.100.1.0/24
add list=vpn_list comment="Network ISP-02" address=10.100.2.0/24
add list=vpn_list comment="Network ISP-02" address=10.100.3.0/24
add list=vpn_list comment="Network ISP-01" address=192.168.100.0/24
add list=vpn_list comment="Network ISP-01" address=192.168.200.0/24
add list=vpn_list comment="Network ISP-01" address=192.168.300.0/24
```

p.s. 
В win не проверял за неимением :)
