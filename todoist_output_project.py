# todoistのプロジェクト一覧を取得する
import json
import requests

url = "https://api.todoist.com/rest/v1/projects"

print("接続開始")
# 自分のtokenを設定する
token = "Bearer xxxxxxxxxx"
content = "application/json"

headers = {'Content-Type': content, 'Authorization': token}
r = requests.get(url = url, headers=headers)

data = json.loads(r.text)

print('処理開始')
try:
    # 出力先がハードコーディング
    file = open('output_project.csv', 'w', encoding="utf-8")
    for key in data:
        id = str(key['id']) or ""
        name = key['name'] or ""
        s = id + "," + name
        file.write(s)
        file.write("\r")
    file.close()
    print('処理終了')
except:
    import traceback
    print('error detail :')
    traceback.print_exc()
