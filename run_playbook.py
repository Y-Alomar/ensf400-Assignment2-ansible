import ansible_runner
import requests



r = ansible_runner.run(private_data_dir='.', inventory='hosts.yml',playbook='hello.yml')

print("Playbook Execution Status:")
print("Status:", r.status)
print("RC:", r.rc)

print("\nVerifying NodeJS Server Response:")
nodejs_servers = ["http://0.0.0.0"]  

for server in nodejs_servers:
    try:
        response = requests.get(server)
        if response.status_code == 200:
            print(f"NodeJS server at {server} is reachable and responding correctly.")
        else:
            print(f"NodeJS server at {server} returned status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"NodeJS server at {server} is unreachable.")