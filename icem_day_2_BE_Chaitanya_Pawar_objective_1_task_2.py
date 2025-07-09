# Name: Chaitany Pawar

#Task 2 use map inside another map for a nested list
words = [["hello", "world"], ["good", "morning"], ["python", "rocks"]]
result = list(map(lambda sublist: list(map(str.upper, sublist)), words))
print(result)
