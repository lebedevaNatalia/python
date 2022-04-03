tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9A', '7B', '9Б', '9B', '8Б', '10A', '10Б', '9A'
]

from itertools import islice

generator = ((tutor, klass) for tutor, klass in zip(tutors, klasses) if len(tutor) > 0)
print(*islice(generator, len(tutors)))