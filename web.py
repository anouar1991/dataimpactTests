from urllib3 import PoolManager
import json
if __name__ == '__main__':
    req = {
        'header': {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'
        },
        'url': 'https://httpbin.org/anything',
        'data': {
            'msg': 'welcomeuser',
            'isadmin': 1
        }
    }

    http = PoolManager()
    res = http.request(
        'POST',
        req['url'],
        fields=req['data'],
        headers=req['header']
    )

    print(json.loads(res.data.decode('utf-8'))['headers'])
