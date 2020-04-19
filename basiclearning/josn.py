import json
jsonstring='[{"user": "qq342517845", "type": "friend::gh", "data": {"gh_id": "gh_79e794fa6bf2", "gh_id_search": "hzins4006788618", "gh_name": "慧择保险网", "gh_avatar": "http://wx.qlogo.cn/mmhead/Q3auHgzwzM6NJGut2xHM0mUSsk1v2AxdMbMJ5eS1PEMprJtbEE71OA/132"}},{"user": "qq342517845", "type": "friend::gh", "data": {"gh_id": "gh_1170ff8d07d9", "gh_id_search": "WeSure100", "gh_name": "微保", "gh_avatar": "http://wx.qlogo.cn/mmhead/Q3auHgzwzM52J0ZPK65a1qo5th1VBox5DhfiarzaPA91VSw1h2Q4Dqg/132"}},{"user": "qq342517845", "type": "friend::person", "data": {"wx_id": "chipueng", "wx_id_search": "chipueng", "wx_nickname": "Chi Pueng", "wx_avatar": "http://wx.qlogo.cn/mmhead/ver_1/ZK4KXWXgmadtTMAIsj1mq1YKlEiapcrtEN5miaH70GEyZ8T8rrYeXaiaWiaS1WVWtOyTtxTgsYPyrbicMCFklKpPv6Q/132", "remark_name": "付志平"}},{"user": "qq342517845", "type": "friend::person", "data": {"wx_id": "Novia1210", "wx_id_search": "Novia1210", "wx_nickname": "??NoNo??", "wx_avatar": "http://wx.qlogo.cn/mmhead/ver_1/iaaZCe2QLfPuBTMWr2CcBTPQkDm8XOwjKLMgAShhE8w6A0htHpMbToJiccm9VsZq45OXYiak6NSvaXes5noW5xFDw/132", "remark_name": "未来"}}]'

# jsonstring='{"user": "qq342517845", "type": "friend::gh", "data": {"gh_id": "gh_79e794fa6bf2", "gh_id_search": "hzins4006788618", "gh_name": "慧择保险网", "gh_avatar": "http://wx.qlogo.cn/mmhead/Q3auHgzwzM6NJGut2xHM0mUSsk1v2AxdMbMJ5eS1PEMprJtbEE71OA/132"}}'
text = json.loads(jsonstring)
for user in text:
    diuser=dict(user)
    userType=diuser.get("type")
    if userType=='friend::person':
         datainfor=diuser.get("data")
         didata=dict(datainfor)
         print(didata.get("wx_nickname")+"       "+didata.get("wx_id_search")+"       "+didata.get("remark_name"))
print(type(text))
# print(text)