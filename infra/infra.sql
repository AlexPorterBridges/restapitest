CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- =========================
-- Buildings
-- =========================

INSERT INTO buildings (id, address, latitude, longitude, status, created_at, updated_at)
VALUES (uuid_generate_v4(), 'ул. Ленина, д.1', 55.7558, 37.6176, 'ACTIVE', NOW(), NOW()),
       (uuid_generate_v4(), 'ул. Пушкина, д.10', 59.9343, 30.3351, 'ACTIVE', NOW(), NOW()),
       (uuid_generate_v4(), 'пр. Мира, д.5', 56.8389, 60.6057, 'ACTIVE', NOW(), NOW()),
       (uuid_generate_v4(), 'ул. Советская, д.3', 55.0415, 82.9346, 'ACTIVE', NOW(), NOW()),
       (uuid_generate_v4(), 'ул. Горького, д.7', 54.7388, 55.9721, 'ACTIVE', NOW(), NOW());

DO
$$
    DECLARE
        activity_id_1      UUID := uuid_generate_v4();
        activity_id_2      UUID := uuid_generate_v4();
        activity_id_3      UUID := uuid_generate_v4();
        activity_id_4      UUID := uuid_generate_v4();
        activity_id_5      UUID := uuid_generate_v4();
        organization_id_1  UUID := uuid_generate_v4();
        organization_id_2  UUID := uuid_generate_v4();
        organization_id_3  UUID := uuid_generate_v4();
        organization_id_4  UUID := uuid_generate_v4();
        organization_id_5  UUID := uuid_generate_v4();
        organization_id_6  UUID := uuid_generate_v4();
        organization_id_7  UUID := uuid_generate_v4();
        organization_id_8  UUID := uuid_generate_v4();
        organization_id_9  UUID := uuid_generate_v4();
        organization_id_10 UUID := uuid_generate_v4();
        organization_id_11 UUID := uuid_generate_v4();
        organization_id_12 UUID := uuid_generate_v4();
        organization_id_13 UUID := uuid_generate_v4();
        organization_id_14 UUID := uuid_generate_v4();
        organization_id_15 UUID := uuid_generate_v4();
        organization_id_16 UUID := uuid_generate_v4();
        organization_id_17 UUID := uuid_generate_v4();
        organization_id_18 UUID := uuid_generate_v4();
        organization_id_19 UUID := uuid_generate_v4();
        organization_id_20 UUID := uuid_generate_v4();

    BEGIN
        INSERT INTO activities (id, name, parent_id, level, status, created_at, updated_at)
        VALUES (activity_id_1, 'Продукты', NULL, 1, 'ACTIVE', NOW(), NOW()),
               (activity_id_2, 'Электроника', NULL, 1, 'ACTIVE', NOW(), NOW()),
               (activity_id_3, 'Молочные продукты', activity_id_1, 2, 'ACTIVE', NOW(), NOW()),
               (activity_id_4, 'Компьютеры', activity_id_2, 2, 'ACTIVE', NOW(), NOW()),
               (activity_id_5, 'Ремонт компьютеров', activity_id_4, 3, 'ACTIVE', NOW(), NOW());

        INSERT INTO organizations (id, name, building_id, status, created_at, updated_at)
        VALUES (organization_id_1, 'ООО Ромашка', (SELECT id FROM buildings LIMIT 1 OFFSET 0), 'ACTIVE', NOW(), NOW()),
               (organization_id_2, 'ЗАО Вектор', (SELECT id FROM buildings LIMIT 1 OFFSET 1), 'ACTIVE', NOW(), NOW()),
               (organization_id_3, 'ООО Сфера', (SELECT id FROM buildings LIMIT 1 OFFSET 2), 'ACTIVE', NOW(), NOW()),
               (organization_id_4, 'ИП Петров', (SELECT id FROM buildings LIMIT 1 OFFSET 3), 'ACTIVE', NOW(), NOW()),
               (organization_id_5, 'ООО Альфа', (SELECT id FROM buildings LIMIT 1 OFFSET 4), 'ACTIVE', NOW(), NOW()),
               (organization_id_6, 'ЗАО Бета', (SELECT id FROM buildings LIMIT 1 OFFSET 0), 'ACTIVE', NOW(), NOW()),
               (organization_id_7, 'ООО Гамма', (SELECT id FROM buildings LIMIT 1 OFFSET 1), 'ACTIVE', NOW(), NOW()),
               (organization_id_8, 'ИП Иванов', (SELECT id FROM buildings LIMIT 1 OFFSET 2), 'ACTIVE', NOW(), NOW()),
               (organization_id_9, 'ООО Дельта', (SELECT id FROM buildings LIMIT 1 OFFSET 3), 'ACTIVE', NOW(), NOW()),
               (organization_id_10, 'ООО Эко', (SELECT id FROM buildings LIMIT 1 OFFSET 4), 'ACTIVE', NOW(), NOW()),
               (organization_id_11, 'ООО Зенит', (SELECT id FROM buildings LIMIT 1 OFFSET 0), 'ACTIVE', NOW(), NOW()),
               (organization_id_12, 'ООО Омега', (SELECT id FROM buildings LIMIT 1 OFFSET 1), 'ACTIVE', NOW(), NOW()),
               (organization_id_13, 'ИП Сидоров', (SELECT id FROM buildings LIMIT 1 OFFSET 2), 'ACTIVE', NOW(), NOW()),
               (organization_id_14, 'ООО Титан', (SELECT id FROM buildings LIMIT 1 OFFSET 3), 'ACTIVE', NOW(), NOW()),
               (organization_id_15, 'ООО Астра', (SELECT id FROM buildings LIMIT 1 OFFSET 4), 'ACTIVE', NOW(), NOW()),
               (organization_id_16, 'ЗАО Неон', (SELECT id FROM buildings LIMIT 1 OFFSET 0), 'ACTIVE', NOW(), NOW()),
               (organization_id_17, 'ООО Вояж', (SELECT id FROM buildings LIMIT 1 OFFSET 1), 'ACTIVE', NOW(), NOW()),
               (organization_id_18, 'ИП Кузнецов', (SELECT id FROM buildings LIMIT 1 OFFSET 2), 'ACTIVE', NOW(), NOW()),
               (organization_id_19, 'ООО Лидер', (SELECT id FROM buildings LIMIT 1 OFFSET 3), 'ACTIVE', NOW(), NOW()),
               (organization_id_20, 'ООО Престиж', (SELECT id FROM buildings LIMIT 1 OFFSET 4), 'ACTIVE', NOW(), NOW());

        INSERT INTO organization_activities (organization_id, activity_id, created_at, updated_at)
        VALUES (organization_id_1, activity_id_1, NOW(), NOW()),
               (organization_id_2, activity_id_2, NOW(), NOW()),
               (organization_id_3, activity_id_3, NOW(), NOW()),
               (organization_id_4, activity_id_4, NOW(), NOW()),
               (organization_id_5, activity_id_5, NOW(), NOW()),
               (organization_id_6, activity_id_1, NOW(), NOW()),
               (organization_id_7, activity_id_2, NOW(), NOW()),
               (organization_id_8, activity_id_3, NOW(), NOW()),
               (organization_id_9, activity_id_4, NOW(), NOW()),
               (organization_id_10, activity_id_5, NOW(), NOW()),
               (organization_id_11, activity_id_1, NOW(), NOW()),
               (organization_id_12, activity_id_2, NOW(), NOW()),
               (organization_id_13, activity_id_3, NOW(), NOW()),
               (organization_id_14, activity_id_4, NOW(), NOW()),
               (organization_id_15, activity_id_5, NOW(), NOW()),
               (organization_id_16, activity_id_1, NOW(), NOW()),
               (organization_id_17, activity_id_2, NOW(), NOW()),
               (organization_id_18, activity_id_3, NOW(), NOW()),
               (organization_id_19, activity_id_4, NOW(), NOW()),
               (organization_id_20, activity_id_5, NOW(), NOW());
    END
$$;

INSERT INTO phones (id, organization_id, number, created_at, updated_at)
SELECT uuid_generate_v4(), o.id, '123-456-78' || i, NOW(), NOW()
FROM organizations o,
     generate_series(1, 3) AS s(i);