vertices = [
    (1, ('M', 'USA', 'Professor')),
    (2, ('F', 'USA', 'Doctor')),
    (3, ('M', 'China', 'Engineer')),
    (4, ('M', 'SG', 'Engineer')),
    (5, ('F', 'SG', 'Professor')),
    (6, ('M', 'SG', 'Doctor')),
    (7, ('F', 'China', 'Engineer')),
    (8, ('F', 'China', 'Doctor')),
    (9, ('M', 'USA', 'Doctor'))
]

edges = [
    (1, 2, ('2008', 'Family', 9)),
    (1, 4, ('2010', 'Friend', 7)),
    (1, 5, ('2011', 'Colleague', 9)),
    (2, 3, ('2011', 'Friend', 7)),
    (2, 4, ('2011', 'Friend', 4)),
    (3, 4, ('2008', 'Friend', 8)),
    (3, 7, ('2011', 'Colleague', 8)),
    (3, 6, ('2012', 'Family', 3)),
    (4, 5, ('2009', 'Family', 9)),
    (4, 6, ('2010', 'Friend', 6)),
    (5, 6, ('2010', 'Family', 8)),
    (5, 9, ('2012', 'Friend', 8)),
    (6, 7, ('2008', 'Friend', 7)),
    (6, 8, ('2012', 'Colleague', 9)),
    (6, 9, ('2012', 'Friend', 5)),
    (7, 8, ('2011', 'Friend', 5)),
    (8, 9, ('2012', 'Colleague', 8))
]