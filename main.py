import random

import requests

SEARCH_API = "http://aweme.snssdk.com//aweme/v1/discover/search/?device_id={}&aid=1128&cursor=0&" \
             "search_source=discover&query_correct_type=1&count=1&keyword={}&hot_search=0&type=1"
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.108 Safari/537.36'}


def generate_nonce():
    nonce = ''
    for i in range(8):
        nonce += str(random.randint(0, 9))
    return nonce


nonce = generate_nonce()


def douyin_name_to_uid(user_name):
    data = requests.get(SEARCH_API.format(nonce, user_name), headers=HEADERS).json()
    try:
        user_uid = data['user_list'][0]['user_info']['uid']
        return user_uid
    except IndexError:
        pass
    return None


if __name__ == '__main__':
    douyin_name = input('请输入抖音号:')
    douyin_uid = douyin_name_to_uid(douyin_name)
    if douyin_uid:
        print(f'用户[{douyin_name}]的UID为:{douyin_uid}')
    else:
        print('查找失败!')
