from json_to_dict import json_to_dict
from dict_to_yaml import dict_to_yaml

rezult = dict_to_yaml(json_to_dict("../timetable.json"))

out = open("timetable_3.yaml", "w", encoding="utf-8")
out.write(rezult)
out.close()

out = open("../output/timetable_3.yaml", "w", encoding="utf-8")
out.write(rezult)
out.close()


