def binary_search(number_to_find, left, right, target):
	if right >= left:
		middle = left + (right - left) // 2
		if(number_to_find[middle] == target):
			return middle
		elif(middle > target):
			return binary_search(number_to_find, left, middle - 1, target)
		else:
			return binary_search(number_to_find, middle + 1, right, target)
	return -1

myList = []
continuing = 'Y'

while (continuing == 'Y' or continuing == 'y'):
	try:
		x = float(input("Enter a number to add to the list "))
		myList.append(x)
		continuing = input("Do you want to continue ? Y/N ")
	except ValueError:
		print("Enter a number")

myList.sort()

while True:
	inp = input("Enter a number to search ")
	try:
		target = float(inp)
		break
	except ValueError:
		print("Enter a number")

result = binary_search(myList, 0, len(myList)-1, target)

print(myList)
if result != -1:
	print("The number has been found at index {0}".format(result))
else:
	print("The number has not been found")


