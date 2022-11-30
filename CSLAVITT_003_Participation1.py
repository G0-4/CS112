length = float(input('Length: '))
width = float(input('width: '))
num_pages = float(input('Number of Pages: '))
height = 0.05

area = length * width
volume = length * width * height * num_pages

print('Area is:', area)
print('Total Volume of Book is: ', volume)