class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def hm_avg(self):
        summ = 0
        calc = 0

        for i in self.grades.values():
            for j in i:
                summ += j

        for k in self.grades.values():
            for l in k:
                calc += 1

        avg = summ / calc
        return round(avg, 1)

    def __str__(self):
        separator = ', '
        joined_prog = separator.join(self.courses_in_progress)
        joined_fin = separator.join(self.finished_courses)
        return f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.hm_avg()}\nКурсы' \
               f' в процессе изучения: {joined_prog}\nЗавершенные курсы: {joined_fin}'

    def __lt__(self, other):
        result = self.hm_avg() < other.hm_avg()

        if not isinstance(other, Student):
            return print('Not a student')

        if result == False:
            return f'При сравнении оценок выиграл -  {self.name}'

        elif result == True:
            return f'При сравнении оценок выиграл - {other.name}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def lec_avg(self):
        summ = 0
        calc = 0

        for i in self.grades.values():
            for j in i:
                summ += j

        for k in self.grades.values():
            for _ in k:
                calc += 1

        avg = summ / calc
        return round(avg, 1)

    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.lec_avg()}'

    def __lt__(self, other):
        result = self.lec_avg() < other.lec_avg()

        if not isinstance(other, Lecturer):
            return print('Not a lecture')

        if result == False:
            return f'\nПри сравнении оценок победил - {self.name}'

        elif result == True:
            return f'\nПри сравнении оценок победил - {other.name}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

second_best_student = Student('James', 'King', 'male')
second_best_student.courses_in_progress += ['Python']
second_best_student.courses_in_progress += ['Git']
second_best_student.finished_courses += ['Введение в программирование']

third_best_student = Student('Miya', 'Jass', 'female')
third_best_student.courses_in_progress += ['C++']
third_best_student.finished_courses += ['Введение в C++']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

second_cool_reviewer = Reviewer('Kent', 'Clark')
second_cool_reviewer.courses_attached += ['Python']

third_cool_reviewer = Reviewer('Jessi', 'Roms')
third_cool_reviewer.courses_attached += ['C++']

cool_lecture = Lecturer('Alex', 'Alan')
cool_lecture.courses_attached += ['Python']

second_cool_lecture = Lecturer('Dima', 'Hush')
second_cool_lecture.courses_attached += ['Python']

cool_lecture.rate_st(best_student, 'Python', 10)
cool_lecture.rate_st(best_student, 'Python', 10)
cool_lecture.rate_st(best_student, 'Python', 6)

second_cool_lecture.rate_st(best_student, 'Python', 4)
second_cool_lecture.rate_st(best_student, 'Python', 9)
second_cool_lecture.rate_st(best_student, 'Python', 8)

cool_reviewer.rate_hw(second_best_student, 'Python', 10)
cool_reviewer.rate_hw(second_best_student, 'Python', 8)
cool_reviewer.rate_hw(second_best_student, 'Python', 7)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

third_cool_reviewer.rate_hw(third_best_student, 'C++', 9)

print(cool_reviewer)
print(cool_lecture)
print(best_student.grades)
print(cool_lecture.lec_avg())
print(best_student)
print(cool_lecture.__lt__(second_cool_lecture))
print(third_best_student)

student_list = [best_student, second_best_student, third_best_student]
lecture_list = [cool_lecture, second_cool_lecture]


def avg_grades_student(list_st, course):
    sum_all = 0
    calc = 0
    for i in list_st:
        if course in i.courses_in_progress:
            for j in i.grades.values():
                for k in j:
                    calc += 1
                    sum_all += k
    formula = sum_all / calc
    correct = round(formula, 1)
    print(f'Среднее значение оценок студентов на курсе {course} - {correct}')


def avg_grades_lecture(list_lc, course):
    sum_all = 0
    calc = 0
    for i in list_lc:
        if course in i.courses_attached:
            for j in i.grades.values():
                for k in j:
                    calc += 1
                    sum_all += k
    formula = sum_all / calc
    correct = round(formula, 1)
    print(f'Среднее значение оценок лекторов на курсе {course} - {correct}')

avg_grades_student(student_list, 'Python')
avg_grades_lecture(lecture_list, 'Python')