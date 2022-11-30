
att_score = int(input('Student\'s Attendance Score: '))
att_total = int(input('What is the total score possible? '))
quiz_1 = int(input('Student\'s Quiz 1 Score: '))
quiz_2 = int(input('Student\'s Quiz 2 Score: '))
quiz_3 = int(input('Student\'s Quiz 3 Score: '))
quiz_4 = int(input('Student\'s Quiz 4 Score: '))
quiz_total = int(input('Total score possible for each quiz? '))
mid = int(input('Studen\'s Midterm Score: '))
mid_total = int(input('Total score possible for the midterm? '))
fin = int(input('Student\'s final score: '))
fin_total = int(input('Total score possible for the final? '))

quiz_list = [quiz_1, quiz_2, quiz_3, quiz_4]
quiz_list.remove(min(quiz_list))

attendance = float((att_score / att_total) * 10)
quiz = float((((quiz_list[0] + quiz_list[1] + quiz_list[2]) / (quiz_total * 3)) *15))
midterm = float((mid/mid_total)*25)
final = float((fin/fin_total)*50)
total = float(attendance + quiz + midterm + final)

print('Attendance:', str(attendance) + '%')
print('Quiz:', str(quiz) + '%')
print('Mid:', str(midterm) + '%')
print('Final:', str(final) + '%')
print('Total Score:', str(total) + '%')

