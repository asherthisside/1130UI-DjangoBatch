import json

with open('countries.json') as f:
    # print(f)
    data = json.load(f)
    # print(type(data))
    # print(data[0]['Country'])

    # count = 0
    # for i in data:
    #     country_name = i['Country']
    #     print(country_name)
    #     count += 1

    # print(count)
    # if country_name == "Japan":
    #     break 

# print(data)

employees = [
    {
        "name" : "Haaris",
        "salary" : 234567,
        "deptt" : "IT",
        "languages" : ["C", "C++", "Python"]
    },

    {
        "name" : "Akash",
        "salary" : 23567,
        "deptt" : "IT",
        "languages" : ["C", "C++", "Python"]
    },
    
    {
        "name" : "Akanksha",
        "salary" : 234567,
        "deptt" : "IT",
        "languages" : ["C", "C++", "Python"]
    }
]

print(type(employees))
employee_json = json.dumps(employees)
print(employee_json)
print(type(employee_json))