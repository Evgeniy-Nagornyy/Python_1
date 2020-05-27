import json, itertools

with open('text_7.txt', 'r', encoding='utf-8') as f_obj:
    results, total_profit, s = [], 0, 0
    try:
        for i in itertools.count(0):
            str_f = f_obj.readline().split()
            if int(str_f[-2]) - int(str_f[-1]) < 0:
                results += [{str_f[0]: int(str_f[-2]) - int(str_f[-1])}]
            else:
                results += [{str_f[0]: int(str_f[-2]) - int(str_f[-1])}]
                total_profit += int(str_f[-2]) - int(str_f[-1])
                s += 1
    except IndexError:
        results += [{'average_profit': total_profit / s}]
with open('text_7.json', 'w', encoding='utf-8') as f_json:
    json.dump(results, f_json)
print(results)
