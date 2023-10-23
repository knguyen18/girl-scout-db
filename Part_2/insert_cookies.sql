INSERT INTO cookie_types (cookie_name, cost) 
VALUES 
	('Thin Mints', 6), 
	('Samoas', 6),
	('Tagalongs', 6),
	('Trefoils', 6), 
	('Toffeetastic', 6);
	
INSERT INTO ingredients(ingredient_name)
VALUES
	('sugar'),
	('cocoa'),
	('mint oil'),
	('coconut extract'),
	('butter'),
	('peanut oil'),
	('peanut butter');

INSERT INTO cookie_type_ingredients(cookie_type_id, ingredient_id, order_num)
VALUES
	(1, 1, 1),
	(1, 2, 2),
	(1, 3, 3),
	(2, 2, 1),
	(2, 4, 2),
	(2, 1, 3),
	(2, 5, 4),
	(3, 2, 1),
	(3, 1, 2),
	(3, 6, 3),
	(3, 7, 4);
	
INSERT INTO troops(troop_number, founding_date, community)
VALUES
	(1234, '2022-09-01', 'Long Beach'),
	(6789, '2023-01-01', 'Cerritos');
	
INSERT INTO adults(last_name, first_name, birthday)
VALUES
	('Holden', 'James', '1992-06-04'),
	('Lovelace', 'Ava', '1990-10-10'),
	('Byron', 'Lord', '1965-05-13'),
	('Jackson', 'Mary', '1953-01-01');
	
INSERT INTO grade_levels(grade_level)
VALUES
	('K'), ('1'), ('2'), ('3'), ('4'), ('5'), ('6'), ('7'), ('8'), ('9'), ('10'), ('11'), ('12');
	
INSERT INTO scouts(last_name, first_name, birthday, troop_number, grade_level)
VALUES
	('Nagata', 'Naomi', '2017-03-03', 1234, 'K'),
	('Hopper', 'Grace', '2017-01-30', 1234, 'K'),
	('Liskov', 'Barbara', '2014-07-01', 6789, '3'),
	('Sparck Jones', 'Mary', '2013-12-30', 6789, '3');
	
INSERT INTO adult_scouts(adult_id, scout_id)
VALUES
	(1, 1),
	(2, 2),
	(3, 2),
	(3, 3),
	(4, 4);
	
INSERT INTO adult_positions(title)
VALUES
	('Co-leader'),
	('Treasurer'),
	('Cookie Chair');
	
INSERT INTO volunteers(troop_number, adult_position_id, adult_id)
VALUES
	(1234, 1, 1),
	(1234, 2, 2),
	(1234, 3, 2),
	(6789, 1, 3);
	
INSERT INTO troop_allotments(pick_up_date, troop_number)
VALUES
	('2023-01-18', 1234),
	('2023-01-18', 6789),
	('2023-02-15', 6789);

INSERT INTO troop_order_lines(troop_allotment_id, cookie_type_id, cases)
VALUES
	(1, 1, 10),
	(1, 2, 10),
	(1, 3, 10),
	(2, 1, 20),
	(2, 2, 5),
	(2, 3, 10),
	(3, 1, 5),
	(3, 4, 3),
	(3, 5, 1);
	
INSERT INTO scout_allotments(pick_up_date, scout_id)
VALUES
	('2023-01-19', 1),
	('2023-01-19', 2),
	('2023-01-20', 3),
	('2023-02-17', 3),
	('2023-01-20', 4),
	('2023-02-18', 4);

INSERT INTO scout_order_lines(scout_allotment_id, cookie_type_id, boxes)
VALUES
	(1, 1, 36),
	(1, 2, 36),
	(1, 3, 24),
	(2, 1, 30),
	(2, 2, 20),
	(2, 3, 10),
	(3, 1, 120),
	(3, 2, 36),
	(3, 3, 60),
	(4, 4, 36),
	(4, 5, 7),
	(5, 1, 120),
	(5, 2, 24),
	(5, 3, 60),
	(6, 1, 60),
	(6, 5, 5);
	
INSERT INTO payments(scout_id, amount, payment_date)
VALUES
	(1, 540, '2023-03-01'),
	(1, 24, '2023-03-15'),
	(2, 360, '2023-02-01'),
	(3, 1296, '2023-01-31'),
	(3, 198, '2023-02-21'),
	(4, 1614, '2023-03-15');
