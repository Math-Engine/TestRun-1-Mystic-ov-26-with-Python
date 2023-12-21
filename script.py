import json

import sys
import os

sys.set_int_max_str_digits(2147483647)

param = int(sys.argv[1])

os.system(f'git pull -f')

with open('max.json', 'r') as f:
    max_json = json.load(f)
    print(json.dumps(max_json, indent="\t"))

with open('result.json', 'r') as f:
    result_json = json.load(f)
    print(json.dumps(result_json, indent="\t"))

max_json['a'] = int(max_json['a']) + 1
start_max_a = max_json['a']
max_json['b'] = int(max_json['b']) + 1
start_max_b = max_json['b']
max_json['c'] = int(max_json['c']) + 1
start_max_c = max_json['c']
max_json['d'] = int(max_json['d']) + 1
start_max_d = max_json['d']

number_of_changes_to_result = 0

for a in range(int(max_json['a']), int(max_json['a']) + param):
    for b in range(int(max_json['b']), int(max_json['b']) + param):
        for c in range(int(max_json['c']), int(max_json['c']) + param):
            for d in range(int(max_json['d']), int(max_json['d']) + param):
                if a**c - b**d == 2 and c > 1 and d > 1:
                    print(str(a) + "^" + str(c) + " - " + str(b) + "^" + str(d))
                    number_of_changes_to_result = number_of_changes_to_result + 1
                    temp_result = {}
                    temp_result["a"] = str(a)
                    temp_result["b"] = str(b)
                    temp_result["c"] = str(c)
                    temp_result["d"] = str(d)
                    result_json.append(temp_result)

max_json["a"] = str(a)
max_json["b"] = str(b)
max_json["c"] = str(c)
max_json["d"] = str(d)

with open('max.json', 'w') as max_file:
    json.dump(max_json, max_file, indent="  ")

with open('result.json', 'w') as result_file:
    json.dump(result_json, result_file, indent="  ")

os.system(f'git config user.name "github-actions[bot]"')
os.system(f'git config user.email "github-actions[bot]@users.noreply.github.com"')
os.system(f'git add .')

if number_of_changes_to_result == 0:
    commit_message = f"({start_max_a}, {start_max_b}, {start_max_c}, {start_max_d}) ~ ({max_json["a"]}, {max_json["b"]}, {max_json["c"]}, {max_json["d"]}) [{param ** 4}] 까지 확인한 결과, 해가 없음"
else:
    commit_message = f"({start_max_a}, {start_max_b}, {start_max_c}, {start_max_d}) ~ ({max_json["a"]}, {max_json["b"]}, {max_json["c"]}, {max_json["d"]}) [{param ** 4}] 까지 확인한 결과, {number_of_changes_to_result}개의 해를 찾음"

os.system(f'git commit --allow-empty -m "' + commit_message + '"')
os.system(f'git push')
