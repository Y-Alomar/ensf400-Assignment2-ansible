import ansible_runner


r = ansible_runner.run(private_data_dir='.', inventory='hosts.yml', host_pattern='all', module='ping')


print("Hosts Information:")
for host_event in r.events:
    if host_event['event'] == 'runner_on_ok':
        host = host_event['event_data']['host']
        ansible_facts = host_event['event_data']['res']['ansible_facts']
        ip = ansible_facts.get('ansible_host', 'IP address not found')
        groups = ansible_facts.get('group_names', [])
        print(f"Name: {host}, IP: {ip}, Groups: {', '.join(groups)}")


print("\nPing Results:")
for host_event in r.events:
    if host_event['event'] == 'runner_on_ok':
        host = host_event['event_data']['host']
        ping_result = host_event['event_data']['res']['ping']
        print(f"Host: {host}, Result: {ping_result}")
