#HW  L1.1 - Marks

student_count = int(input("Введите количество студентов:"))
student_mark_sum = {}

task_count = int(input("Введите количесво заданий на курсе:"))
rating_task = {}
# инициализация
for i in range(1,task_count+1):
    rating_task[i] = 0

print("Введите имена студентов:")
for i in range(1, student_count + 1):
    name = input(f"Студент {i}: ")
    student_mark_sum[name] = []

print("Введите оценку для каждого задания от 0 до 10")
for student_name in student_mark_sum:
    print(f"Для {student_name}")
    marks_sum = 0;

    for task_name in rating_task:
        mark = int(input(f"\t Задание {task_name}: "))

        if mark < 0 or mark > 10:
            print("Ошибка!")

        marks_sum += mark
        rating_task[task_name] += mark
    student_mark_sum[student_name] = marks_sum

# определение топ-3 заданий
rating_task_last = 3
task_name = list(rating_task.keys())
rating_task_list = list(rating_task.values())
#сортируем
rating_task_sorted = rating_task_list.copy()
rating_task_sorted.sort()

print(f"ТОП-{rating_task_last} сложных заданий")
for i in range(rating_task_last):
    #получаем индекс максимального числа
    ind = rating_task_list.index(rating_task_sorted[i])
    mark = task_name[ind]
    summ = rating_task_sorted[i]
    print(f"Задание {mark}: сумма - {summ}")
    #удаляем из  списков выведенное значение
    task_name.pop(ind)
    rating_task_list.pop(ind)

# определение топ-3 студентов
student_top = 3

student_name = list(student_mark_sum.keys())
student_mark = list(student_mark_sum.values())
#сортируем
student_mark_sorted = student_mark.copy()
student_mark_sorted.sort(reverse=True)

print(f"ТОП-{student_top} лучших студентов")
for i in range(student_top):
    # получаем индекс максимального числа
    ind = student_mark.index(student_mark_sorted[i])
    name = student_name[ind]
    summ = student_mark_sorted[i]
    print(f"Студент {name}: сумма - {summ}")
    # удаляем из  списков выведенное значение
    student_name.pop(ind)
    student_mark.pop(ind)