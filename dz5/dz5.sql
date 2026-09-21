-- Нормализация таблицы StudentGrades до 3НФ

-- Часть 1. Теоретический анализ

-- Первичный ключ исходной таблицы:
-- (student_id, subject_id, exam_date)
--
-- student_id отдельно не подходит, потому что один студент может иметь
-- несколько результатов по разным предметам.
-- subject_id отдельно не подходит, потому что один предмет сдаёт много студентов.
-- exam_date отдельно не подходит, потому что в один день может быть много результатов.
--
-- Основные функциональные зависимости:
-- student_id -> student_name, group_id
-- group_id -> group_name
-- teacher_id -> teacher_name
-- subject_id -> subject_name
-- (student_id, subject_id, exam_date) -> grade
--
-- Транзитивные зависимости:
-- student_id -> group_id -> group_name
-- teacher_id -> teacher_name
-- subject_id -> subject_name
--
-- Исходная таблица находится в 1НФ:
-- значения атомарные, повторяющихся групп нет.
-- До 2НФ она не доходит, потому что неключевые атрибуты зависят
-- только от части составного ключа.
-- Например: student_id -> student_name.
-- Поэтому таблица не находится в 3НФ.

-- Часть 2. Таблицы в 3НФ

CREATE TABLE groups (
    group_id VARCHAR(10) PRIMARY KEY,
    group_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    group_id VARCHAR(10) NOT NULL,
    FOREIGN KEY (group_id) REFERENCES groups(group_id)
);

CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY,
    teacher_name VARCHAR(100) NOT NULL
);

CREATE TABLE subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE grades (
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    teacher_id INT NOT NULL,
    exam_date DATE NOT NULL,
    grade INT NOT NULL,
    PRIMARY KEY (student_id, subject_id, exam_date),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

-- Итоговый список таблиц:
-- groups
-- students
-- teachers
-- subjects
-- grades

-- Схема связей:
--
-- groups 1 ----- N students
-- students 1 --- N grades
-- subjects 1 --- N grades
-- teachers 1 --- N grades
