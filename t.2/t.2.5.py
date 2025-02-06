def smallest_average(person1, person2, person3):
    avg1 = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    avg2 = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    avg3 = (person3["result1"] + person3["result2"] + person3["result3"]) / 3

    if avg1 < avg2 and avg1 < avg3:
        return person1
    if avg2 < avg1 and avg2 < avg3:
        return person2
    return person3

person1 = {"name": "Mary", "result1": 7, "result2": 3, "result3": 8}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))
