import json
import yaml

file = open("../timetable.json", "r", encoding="utf-8")
text = json.load(file)  # В переменную загрузятся данные из json файла
file.close()

# Конвертация и запись
rezult = yaml.dump(text, allow_unicode=True)

out = open("timetable_2.yaml", "w", encoding="utf-8")
out.write(rezult)
out.close()

out = open("../output/timetable_2.yaml", "w", encoding="utf-8")
out.write(rezult)
out.close()


