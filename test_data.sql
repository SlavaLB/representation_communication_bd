-- seed_data.sql - Наполнение тестовыми данными
USE `db_communication`;

-- Очистка таблиц
DELETE FROM person_country;
DELETE FROM phone;
DELETE FROM passport;
DELETE FROM country;
DELETE FROM person;
ALTER TABLE person AUTO_INCREMENT = 1;
ALTER TABLE country AUTO_INCREMENT = 1;
ALTER TABLE passport AUTO_INCREMENT = 1;
ALTER TABLE phone AUTO_INCREMENT = 1;

-- Добавление стран
INSERT INTO `country` (`name`, `created_at`) VALUES
('Россия', NOW()),
('США', NOW()),
('Германия', NOW()),
('Франция', NOW()),
('Япония', NOW()),
('Китай', NOW()),
('Великобритания', NOW()),
('Италия', NOW()),
('Испания', NOW()),
('Канада', NOW());

-- Добавление людей
INSERT INTO `person` (`name`, `created_at`) VALUES
('Иван Иванов', NOW()),
('Мария Петрова', NOW()),
('Алексей Сидоров', NOW()),
('Елена Кузнецова', NOW()),
('Дмитрий Смирнов', NOW()),
('Ольга Васильева', NOW()),
('Сергей Попов', NOW()),
('Анна Новикова', NOW()),
('Павел Морозов', NOW()),
('Татьяна Федорова', NOW());

-- Добавление паспортов (1:1 связь)
INSERT INTO `passport` (`number`, `person_id`, `created_at`) VALUES
('4501123456', 1, NOW()),
('4501987654', 2, NOW()),
('4501567890', 3, NOW()),
('4501345678', 4, NOW()),
('4501901234', 5, NOW()),
('4501789012', 6, NOW()),
('4501456789', 7, NOW()),
('4501123987', 8, NOW()),
('4501654321', 9, NOW()),
('4501876543', 10, NOW());

-- Добавление телефонов (1:M связь)
-- (если у phone тоже есть created_at)
INSERT INTO `phone` (`number`, `type`, `person_id`, `created_at`) VALUES
('+7-916-123-45-67', 'личный', 1, NOW()),
('+7-916-987-65-43', 'рабочий', 1, NOW()),
('+7-916-555-55-55', 'личный', 2, NOW()),
('+1-212-555-01-02', 'рабочий', 2, NOW()),
('+7-916-777-88-99', 'личный', 3, NOW()),
('+49-30-1234567', 'рабочий', 3, NOW()),
('+7-916-444-33-22', 'личный', 4, NOW()),
('+33-1-2345-6789', 'рабочий', 4, NOW()),
('+7-916-111-22-33', 'личный', 5, NOW()),
('+7-916-999-88-77', 'рабочий', 5, NOW()),
('+7-916-666-55-44', 'личный', 6, NOW()),
('+44-20-7946-0958', 'рабочий', 6, NOW()),
('+7-916-333-22-11', 'личный', 7, NOW()),
('+39-06-6987-6543', 'рабочий', 7, NOW()),
('+7-916-222-11-00', 'личный', 8, NOW()),
('+34-91-123-45-67', 'рабочий', 8, NOW()),
('+7-916-000-99-88', 'личный', 9, NOW()),
('+1-416-555-01-02', 'рабочий', 9, NOW()),
('+7-916-888-77-66', 'личный', 10, NOW()),
('+81-3-1234-5678', 'рабочий', 10, NOW());

-- Добавление связей люди-страны (M:M связь)
INSERT INTO `person_country` (`person_id`, `country_id`, `visit_date`, `purpose`, `created_at`) VALUES
(1, 1, '2023-01-15 10:00:00', 'проживание', NOW()),
(1, 2, '2023-06-20 14:30:00', 'отпуск', NOW()),
(1, 3, '2023-09-10 09:15:00', 'командировка', NOW()),
(2, 2, '2023-02-20 11:45:00', 'учеба', NOW()),
(2, 4, '2023-07-15 16:20:00', 'туризм', NOW()),
(3, 3, '2023-03-10 08:30:00', 'работа', NOW()),
(3, 5, '2023-08-05 13:10:00', 'конференция', NOW()),
(4, 4, '2023-04-05 12:00:00', 'отпуск', NOW()),
(4, 6, '2023-10-25 15:45:00', 'бизнес', NOW()),
(5, 5, '2023-05-12 09:30:00', 'стажировка', NOW()),
(5, 7, '2024-01-10 11:20:00', 'встреча', NOW()),
(6, 6, '2023-06-18 14:15:00', 'экскурсия', NOW()),
(6, 8, '2024-02-15 10:45:00', 'семинар', NOW()),
(7, 7, '2023-07-22 16:30:00', 'переговоры', NOW()),
(7, 9, '2024-03-20 13:25:00', 'выставка', NOW()),
(8, 8, '2023-08-30 08:45:00', 'отпуск', NOW()),
(8, 10, '2024-04-05 15:10:00', 'конференция', NOW()),
(9, 9, '2023-09-14 12:30:00', 'работа', NOW()),
(9, 1, '2024-05-12 09:15:00', 'визит', NOW()),
(10, 10, '2023-10-28 11:00:00', 'обучение', NOW()),
(10, 2, '2024-06-08 14:50:00', 'встреча', NOW());

-- Проверка данных
SELECT 'Таблица person:' AS '';
SELECT * FROM person;

SELECT 'Таблица passport:' AS '';
SELECT * FROM passport;

SELECT 'Таблица phone:' AS '';
SELECT * FROM phone;

SELECT 'Таблица country:' AS '';
SELECT * FROM country;

SELECT 'Таблица person_country:' AS '';
SELECT * FROM person_country;

-- Пример сложного запроса
SELECT 'Люди с их телефонами и странами:' AS '';
SELECT 
    p.name AS person_name,
    pa.number AS passport_number,
    ph.number AS phone_number,
    ph.type AS phone_type,
    c.name AS country_name,
    pc.visit_date,
    pc.purpose
FROM person p
LEFT JOIN passport pa ON p.id = pa.person_id
LEFT JOIN phone ph ON p.id = ph.person_id
LEFT JOIN person_country pc ON p.id = pc.person_id
LEFT JOIN country c ON pc.country_id = c.id
ORDER BY p.name, ph.type, c.name;