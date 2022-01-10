import requests
#
# response = requests.request('GET', 'https://www.python.org/wwww')
#
# print('--->', response)
# print(dir(response))
# print(response.request.url)
# print(response.headers)
# print(response.text)
# print(response.status_code)
#
# response = requests.get('https://www.python.org')
#
# print(response.headers['Content-Type'])
#
# with open('test.html', 'wb') as f:
#     f.write(response.content)
#
# try:
#     response = requests.get('https://kuna.io/api/v2/tickers/btcuah')
# except:
#     pass
#
# # response.status_code ?? 200
#
# # response.headers ?? 'application/json'
# try:
#     print(response.json())
# except:
#     pass
#
# print(response.headers)
# print(response.text)
# print(response.json())
#
# res = response.json()

# url = 'https://webhook.site/ff89df7c-04b6-4c5e-acef-912faa125c31'
#
# heraders = {'header1': '123456'}
#
# body = {'aa': 'bb', 'cc': 'dd'}
#
# params = {'param1': 'zzz', 'param2': 'rrr'}
#
# res = requests.get(url, headers=heraders, json=body, params=params)
#
#
# url = 'https://www.google.com/search'
#
#
# res = requests.get(url, params={'q': 'it+Hillel'})
#
# with open('search.html', 'wb') as f:
#     f.write(res.content)
#
# res = requests.get('https://www.python.org/static/img/python-logo@2x.png')
# print(res.content)

# with open('icon.png', 'wb') as f:
#     f.write(res.content)

# file = open('example.txt', 'a')
# file.write('aaaaaaaa1234567890')
# file.close()


# file = open('example.txt', 'rb')
# for line in file:
#     print(line)
# file.close()
#
# with open('example.txt', 'rb') as file:
#     pass
