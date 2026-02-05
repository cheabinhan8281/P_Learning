'''
http://api.openweathermap.org/geo/1.0/direct?q=성남시,KR&limit=&appid=b0def4f724cfb0404a64afc89ab26618
'''

import requests
res = requests.get('http://api.openweathermap.org/geo/1.0/direct?q=성남시,KR&limit=&appid=b0def4f724cfb0404a64afc89ab26618')
print(res.json())