from typing import List, Any, Union

from base64py import jpg_to_base64
import time
from aip import AipFace

APP_ID = '16003091'
API_KEY = 'AQQAUfB61ovAysOMEh7TILWF'
SECRET_KEY = 'b03ilm1soYDVt5U1rLtWdHHnSWbaSNBY'

client = AipFace(APP_ID,API_KEY,SECRET_KEY)

def face_search(group_id, img_src):
    # img_src = 'base64py/1.jpg'
    img_in_base64 = jpg_to_base64.img_to_base64(img_src)
    # print(img_in_base64)
    img_Type = "BASE64"
    # Group_id = "09141502"
    try:
        search_result = client.search(img_in_base64, img_Type, group_id)
        error_code = search_result['error_code']
        error_msg = search_result['error_msg']
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(search_result['timestamp']))
        user_list = search_result['result']['user_list']
        result = {}
        for i in user_list:  # i就代表了user_list中的一个变量
            user_id = i['user_id']
            score = i['score']
            print(user_id)
            print(score)
            print(now_time)


        # print(error_code)
        print(search_result)
        # options = {}
        # options["quality_control"] = "NORMAL"
        # options["liveness_control"] = "NONE"
    except:
        user_list = []
    return user_list
