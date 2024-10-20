import json

f = open('E:/projects/RPS_telegram-bot/database/user_data_txt', 'r')
data1 = f.read()
data = json.loads(data1)
f.close()

info: dict[str, list[int, int, int]] = data
# Значения равны соответственно ПОБЕДАМ, ПОРАЖЕНИЯМ, КОЛ-ВУ ИГР
