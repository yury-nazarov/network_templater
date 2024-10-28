from pathlib import Path


def main():
    network_objects = file_open("networks/")
    mikrotik_templater(network_objects)


def file_open(dir_path: str) -> list[dict]:
    """
    Читает все файлы в дирректории и формирует из них структуру данных
    [
        {'vpn_list': 'vpn_list', 'description': 'ISP-01', 'networks': ['192.168.100.0/24', '192.168.200.0/24']},
        {'vpn_list': 'vpn_list', 'description': 'ISP-02', 'networks': ['10.100.1.0/24', '10.100.2.0/24']}
    ]
    """
    network_objects = []

    dp = Path(dir_path)

    for f in dir_path:
        file_names = [f for f in dp.iterdir() if f.is_file()]

    for file_name in file_names:
        with open(file_name) as f:
            data = dict()
            data["vpn_list"] = f.readline().strip()
            data["description"] = f.readline().strip()
            data["networks"] = [i.strip() for i in f.readlines() if i.strip()]
        network_objects.append(data)

    return network_objects


def mikrotik_templater(network_objects: list[dict]):
    """ Вернет в stdout конфиг в формате Mikrotic """
    print("/ip firewall address-list")
    for line in network_objects:
        for network in line.get('networks'):
            print(f'add list={line.get('vpn_list')} comment="{line.get('description')}" address={network}')


if __name__ == '__main__':
    main()
