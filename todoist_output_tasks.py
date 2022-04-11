import json
from datetime import datetime as dt
from importlib.resources import contents
import requests

# ここで指定した日付以降に作ったタスクを抽出する
targetDay = dt.strptime("2022-03-01",'%Y-%m-%d')

tasks_url = "https://api.todoist.com/rest/v1/tasks"
projects_url = "https://api.todoist.com/rest/v1/projects"
sections_url = "https://api.todoist.com/rest/v1/sections"

print("接続開始")
# 自分のtokenを設定する
token = "Bearer XXXXXXXXXX"
content = "application/json"

headers = {'Content-Type': content, 'Authorization': token}
r = requests.get(url = tasks_url, headers=headers)

tasks_data = json.loads(r.text)

r = requests.get(url = projects_url, headers=headers)

projects_data = json.loads(r.text)

r = requests.get(url = sections_url, headers=headers)

sections_data = json.loads(r.text)

print('処理開始')
try:
    # 出力先がハードコーディング
    file = open('.\output_tasks.csv', 'w', encoding="utf-8")
    for key in tasks_data:
        created = key['created'] or ""
        created10 = created[:10]
        createDay = dt.strptime(created10,'%Y-%m-%d') 
        # 指定の日付以降のタスクを抽出
        if targetDay <= createDay:
            name = ""
            for project in projects_data:
                # プロジェクトIDからプロジェクト名を当てる
                project_id = str(key['project_id']) or ""
                if project_id == (str(project['id']) or "" ):
                    name = project['name'] or ""
            contents = key['content'] or ""
            description = key['description'] or ""
            sectionName = ""
            for section in sections_data:
                # セクションIDからセクション名を当てる
                section_id = str(key['section_id']) or ""
                if section_id == (str(section['id']) or ""):
                    sectionName = section['name'] or ""
            s = "\"" + contents + "\",\"" + description + "\"," + name + "," + sectionName
            file.write(s)
            file.write("\r")
    file.close()
    print('処理終了')
except:
    import traceback
    print('error detail :')
    traceback.print_exc()
