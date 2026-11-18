#ques 1
movies = ["kabhi khushi kabhi gham","flying jatt","hum apke hai kon","heeropanti","KGF"]
print(movies[2])

# ques 2
num = [77,55,888,66,44]
num.insert(3,67)
num.remove(77)
print(num)
print(f"maximum numbeer is {max(num)}")

#ques 3
marks =[ 45,67,95,96,65]
average = sum(marks)/len(marks)
print(average)

# ques 4
num2 =[ 44,65,6,3,45,667,54,67,88,33,54,778,9,8,55,43]
for i in num2:
    if i % 2 == 0:
        print(i)


Students = ["mukti","ram","shayam","jayant","ganseh"]
marks2 = [87,45,66,76,45]
for i in range(5):
    print(f" {Students[i]}'s marks is {marks2[i]}")
average2 = sum(marks2)/len(marks2)
print(f" Average score is {average2}")
y = marks2.index(max(marks2))
print(f"highest score is {max(marks2)} scored by {Students[y]}")