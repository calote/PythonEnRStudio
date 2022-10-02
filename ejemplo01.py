x = [1, 2, 3]
y = x    # `y` and `x` now refer to the same list!
x.append(4)
print("x is", x)
print("y is", y)


x = [1]
x
x + x
x * 3


x = [1, 2, 3]
x[0]
x[1]
x[2]


x = [1, 2, 3]
x[-1]
x[-2]
x[-3]

x = [1, 2, 3, 4, 5, 6]
x[0:2] # get items at index positions 0, 1
x[1:]  # get items from index position 1 to the end
x[:-2] # get items from beginning up to the 2nd to last.
x[:]   # get all the items 
x[::2] # get all the items, with a stride of 2
x[1::2] # get all the items from index 1 to the end, with a stride of 2



def my_function(name = "World"):
  print("Hello", name)

my_function()
my_function("Friend")
