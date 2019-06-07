from aip import AipFace

APP_ID = '16003091'
API_KEY = 'AQQAUfB61ovAysOMEh7TILWF'
SECRET_KEY = 'b03ilm1soYDVt5U1rLtWdHHnSWbaSNBY'

client = AipFace(APP_ID,API_KEY,SECRET_KEY)

def Dele_group(Group_id):
    result = client.groupDelete(Group_id)
    return result['error_msg']

def Add_group(Group_id):
    result = client.groupAdd(Group_id)
    return result['error_msg']

def Query_group():
    result = client.getGroupList()
    # print(result)
    grouplist = result['result']['group_id_list']
    # print(grouplist)
    return grouplist

# Query_group()