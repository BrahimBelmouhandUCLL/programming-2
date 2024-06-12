# Write your code here
def cakes(eggs, butter, flour):
    neweggs = eggs // 5
    newbutter = butter // 250
    newflour = flour // 250
    minimal = min(neweggs, newbutter, newflour)
    return minimal

print(cakes(18,600,1000))