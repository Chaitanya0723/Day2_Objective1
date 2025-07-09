# Name: Chaitany Pawar

# task 1
def outer(x):
    def inner(y):
        return x+y
    return inner
add20=outer(20)
result=add20(10)
print(result)

#Task 2 use map inside another map for a nested list
words = [["hello", "world"], ["good", "morning"], ["python", "rocks"]]
result = list(map(lambda sublist: list(map(str.upper, sublist)), words))
print(result)
