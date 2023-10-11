import csv


class Naming:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self._validate(value)
        setattr(instance, self.param_name, value)

    def _validate(self, value):
        result = True
        a = value.split()
        for i in a:
            if not (i.isalpha() and i.istitle()):
                result = False
        if result:
            return value
        raise ValueError(f'ФИО должно состоять только из букв и начинаться с заглавной буквы')


class Student:
    name = Naming()

    def __init__(self, name, subjects_file):
        self.name = name
        self.predmet = self._read_predmet(subjects_file)

    def _read_predmet(self, path):
        result = {}
        with open(path, 'r', newline='', encoding='UTF-8') as f:
            csv_f = csv.reader(f, dialect='excel')
            for i in csv_f:
                for j in list(i):
                    result[j] = {'test': [], 'evaluation': []}
        return result

    def add_grade(self, subject, grade):
        if subject in self.predmet.keys():
            if 2 <= grade <= 5:
                self.predmet[subject]['evaluation'].append(grade)
            else:
                raise ValueError('Оценка должна быть целым числом от 2 до 5')
        else:
            raise Exception('Нет такого предмета')

    def add_test_score(self, subject, test_score):
        if subject in self.predmet.keys():
            self.predmet[subject]['test'].append(test_score)
        else:
            raise Exception('Нет такого предмета')

    def add_subject(self, subject, grade, test_score):
        if subject in self.predmet.keys():
            self.predmet[subject]['evaluation'].append(grade)
            self.predmet[subject]['test'].append(test_score)
        else:
            raise Exception('Нет такого предмета')
        #метод для добавления информации о предмете, оценке и результате теста.

    def get_average_test_score(self, subject):
        if subject in self.predmet.keys():
            return round(sum(self.predmet[subject]['test']) / len(self.predmet[subject]['test']), 1)
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_grade(self):
        ocenki = []
        for k in self.predmet.keys():
            if self.predmet[k]['evaluation']:
                ocenki.extend(self.predmet[k]['evaluation'])
        return round(sum(ocenki)/len(ocenki), 1)
        #метод, возвращающий средний балл студента по всем предметам.

    def get_subjects(self):
        predmeti = []
        for k in self.predmet.keys():
            if self.predmet[k]['evaluation'] or self.predmet[k]['test']:
                predmeti.append(k)
        return predmeti
        #метод, возвращающий список всех предметов, по которым есть информация у студента.

    def __str__(self):
        return f'Студент: {self.name}\nПредметы: {", ".join(self.get_subjects())}'


def get_average_grades(students):
    for i in students:
        print(f'Студенет {i._name}')
        pred = i.get_subjects
        sred = []
        for j in pred:
            sred.append(i.get_average_grade(j))
        print(f'Средний балл {round(sum(sred)/len(sred), 1)}')
    #которая принимает список студентов и выводит информацию о средних баллах для каждого студента.

def get_subject_average(students, subject):
    for i in students:
        print(f'{i._name} по {subject} имеет {i.get_average_grade(subject)}')
    # которая принимает список студентов и название предмета, и выводит информацию о среднем
    # балле по этому предмету для каждого студента.

def get_top_student(students, subject):
    res = []
    for i in students:
        res.append([i._name, i.get_average_grade(subject)])
    m = max(res, key=lambda i: i[1])
    print(m[0])
#которая принимает список студентов и название предмета, и выводит информацию о
#студенте с наивысшим средним баллом по этому предмету.



student = Student("Иван Иванов", "file.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)