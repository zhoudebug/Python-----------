from base64py import jpg_to_base64
from aip import AipFace

APP_ID = '16003091'
API_KEY = 'AQQAUfB61ovAysOMEh7TILWF'
SECRET_KEY = 'b03ilm1soYDVt5U1rLtWdHHnSWbaSNBY'

client = AipFace(APP_ID,API_KEY,SECRET_KEY)

def face_registration(img_src, group_id, user_id):
    image_Type = "BASE64"
    img_in_base64 = jpg_to_base64.img_to_base64(img_src)
    # client.addUser(img_src,image_Type,group_id,user_id)
    options = {}
    options["quality_control"] = "NORMAL"
    options["liveness_control"] = "LOW"
    result = client.addUser(img_in_base64, image_Type, group_id, user_id, options)
    # print(result)
    return result['error_msg']


def face_update(img_src, group_id, user_id):
    image_Type = "BASE64"
    img_in_base64 = jpg_to_base64.img_to_base64(img_src)
    options = {}
    options["quality_control"] = "NORMAL"
    options["liveness_control"] = "LOW"
    result = client.updateUser(img_in_base64,image_Type,group_id,user_id,options)
    return result['error_msg']


def face_delete(group_id, user_id):
    options = {}
    options["quality_control"] = "NORMAL"
    options["liveness_control"] = "LOW"
    result = client.deleteUser(group_id,user_id)
    print(result['error_msg'])
    return result['error_msg']


