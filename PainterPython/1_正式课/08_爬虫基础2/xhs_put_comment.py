import json
import pprint

import re
import execjs
from py_mini_racer import py_mini_racer

def GetXs( cookie, api, data):
    with open('xhs_xs.js', 'r', encoding='utf-8') as f:
        jstext = f.read()

    ctx = execjs.compile(jstext)

    match = re.search(r'a1=([^;]+)', cookie)
    a1 = ""
    if match:
        a1 = match.group(1)
    else:
        print("关键参数a1获取失败，请检查你的cookie")
        return ""

    result = ctx.call("get_xs", api, data, a1)
    return result

if __name__ == '__main__':
    cookie = 'a1=188d903a6ebsycvs1m7p51d1p35280ti6l5nfbzno30000384502; webId=5e66a87d89240eb9783c68d554e87b58; gid=yYYfj8q0iiKyyYYfj8q0K1DudDMvShMy6WU22IlyfyUq2Iq8JY893i888qY428J8yf04Yqdf; gid.sign=t39uBFOVkroHc3CfHLl4FKLUdf0=; customerClientId=187675897385246; web_session=0400695d2a2e627ff8988e60e7364bca07ace1; abRequestId=5e66a87d89240eb9783c68d554e87b58; customer-sso-sid=64dd67656400000000000003; x-user-id-creator.xiaohongshu.com=5655aa2df53ee04a5d81a8ce; access-token-creator.xiaohongshu.com=customer.ares.AT-b092eec4bbe84efb8986c3f174d3d5f8-91ee5aa74f58442eb68f6f645f270b51; amp_6e403e=bHnPVddE_7yjogiSt2fVCj...1h90njmb0.1h90njmb0.0.5.5; webBuild=3.7.0; ajs_user_id=KuV02fSqKPVuBUWqYb9110EqWsu1; ajs_anonymous_id=b454a71c-9d94-4c76-942b-d67184f05749; xsecappid=xhs-pc-web; websectiga=8886be45f388a1ee7bf611a69f3e174cae48f1ea02c0f8ec3256031b8be9c7ee; sec_poison_id=ff658371-8cbf-4454-ae23-720912e6219d'
    api = "/api/sns/web/v1/comment/post"  # comment api
    data = {"note_id": "64e3217e000000001701b062", "content": "很美丽的地方", "at_users": []}
    xs = GetXs(cookie, api, data)
    print(json.dumps(xs, indent=4))

    



    path = "/api/sns/web/v1/user_posted?num=30&cursor=64984cc40000000013015eac&user_id=5655aa2df53ee04a5d81a8ce&image_scenes="