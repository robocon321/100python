import datetime

import requests

TOKEN = 'akdzkd983j'
USERNAME = 'robocon321'
URL = 'https://pixe.la'

# create_body = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes'
# }
#
# create_endpoint = '/v1/users'
#
# createResponse = requests.post(url = f"{URL}{create_endpoint}", json = create_body)
# print(createResponse.text)

graph_endpoint = f"/v1/users/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
#
headers = {
    "X-USER-TOKEN": TOKEN
}
# graphResponse = requests.post(url = f"{URL}{graph_endpoint}", json = graph_config, headers = headers)
# print(graphResponse.text)

# format = '%Y%m%d'
#
# graph_post_config = {
#     "date": datetime.datetime.strftime(datetime.datetime.now(), format),
#     "quantity": str(9.2)
# }
# graph_post_response = requests.post(url = f"{URL}{graph_endpoint}/graph1", json = graph_post_config, headers=headers)
# print(graph_post_response.text)

# graph_put_endpoint = f"/v1/users/robocon321/graphs/graph1/20220807"
# graph_put_config = {
#     "quantity": "20"
# }
# graph_put_response = requests.put(url = f"{URL}{graph_put_endpoint}", json = graph_put_config, headers = headers)
# print(graph_put_response.text)

graph_delete_endpoint = f"/v1/users/robocon321/graphs/graph1/20220808"
graph_delete_response = requests.delete(f"{URL}{graph_delete_endpoint}", headers=headers)
print(graph_delete_response.text)