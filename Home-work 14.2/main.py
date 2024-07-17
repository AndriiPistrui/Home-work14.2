from student import Student
from group import Group
from errors import GroupLimitError

def main():
    st1 = Student('Чоловік', 30, 'Стів', 'Джобс', 'AN142')
    st2 = Student('Жінка', 25, 'Ліза', 'Тейлор', 'AN145')
    st3 = Student('Чоловік', 21, 'Джон', 'Доу', 'AN143')
    st4 = Student('Жінка', 22, 'Джейн', 'Доу', 'AN144')
    st5 = Student('Чоловік', 23, 'Джим', 'Бім', 'AN146')
    st6 = Student('Жінка', 24, 'Джекі', 'Чан', 'AN147')
    st7 = Student('Чоловік', 25, 'Брюс', 'Лі', 'AN148')
    st8 = Student('Жінка', 26, 'Люсі', 'Лю', 'AN149')
    st9 = Student('Чоловік', 27, 'Вілл', 'Сміт', 'AN150')
    st10 = Student('Жінка', 28, 'Анджеліна', 'Джолі', 'AN151')
    st11 = Student('Чоловік', 29, 'Бред', 'Пітт', 'AN152')

    gr = Group('PD1')

    students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]

    for student in students:
        try:
            gr.add_student(student)
        except GroupLimitError as e:
            print(e)

    print(gr)

    assert gr.find_student('Джобс') == st1
    assert gr.find_student('Jobs2') is None

    gr.delete_student('Тейлор')
    print(gr) # Only one student

if __name__ == "__main__":
    main()
