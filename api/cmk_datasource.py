import requests

url = 'http://localhost:3003/api/objects'
response = requests.get(url)
data = response.json()

output = []

for obj_name, obj_data in data.items():
    output.append(f"<<<{obj_name}>>>")
    for metric, value in obj_data.items():
        output.append(f"{metric}: {value}")

print('\n'.join(output))
