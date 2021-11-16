DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS product_series;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    name VARCHAR(255),
    id SERIAL PRIMARY KEY,
    active BOOLEAN
);

CREATE TABLE product_series (
    name VARCHAR(255),
    skill_level VARCHAR(255),
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE,
    id SERIAL PRIMARY KEY
);

CREATE TABLE products (
    colour VARCHAR(255),
    wood VARCHAR (255),
    in_stock INT,
    purchase_cost INT,
    selling_price INT,
    id SERIAL PRIMARY KEY,
    product_series_id INT REFERENCES product_series(id) ON DELETE CASCADE
);

INSERT INTO manufacturers (name, active) VALUES ('DW', True);
INSERT INTO manufacturers (name, active) VALUES ('Pearl', True);
INSERT INTO manufacturers (name, active) VALUES ('Mapex', True);
INSERT INTO manufacturers (name, active) VALUES ('Ludwig', True);


INSERT INTO product_series (name, skill_level, manufacturer_id) VALUES ('Design', 'Intermediate', 1);
INSERT INTO product_series (name, skill_level, manufacturer_id) VALUES ('Performance', 'Pro', 1);
INSERT INTO product_series (name, skill_level, manufacturer_id) VALUES ('Export', 'Beginner', 2);
INSERT INTO product_series (name, skill_level, manufacturer_id) VALUES ('Masters', 'Intermediate', 2);
INSERT INTO product_series (name, skill_level, manufacturer_id) VALUES ('Masterworks', 'Pro', 2);
INSERT INTO product_series (name, skill_level, manufacturer_id) VALUES ('Tornado', 'Beginner', 3);
INSERT INTO product_series (name, skill_level, manufacturer_id) VALUES ('Armory', 'Intermediate', 3);
INSERT INTO product_series (name, skill_level, manufacturer_id) VALUES ('Saturn', 'Pro', 3);
INSERT INTO product_series (name, skill_level, manufacturer_id) VALUES ('Pocket', 'Beginner', 4);
INSERT INTO product_series (name, skill_level, manufacturer_id) VALUES ('NeuSonic', 'Intermediate', 4);
INSERT INTO product_series (name, skill_level, manufacturer_id) VALUES ('Classic', 'Pro', 4);

INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Blue', 'Birch', 1, 1000, 1500, 1);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Black', 'Birch', 10, 900, 1400, 1);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('White', 'Maple', 10, 1800, 2300, 2);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Red Sparkle', 'Maple', 10, 2000, 2500, 2);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Black', 'Birch', 10, 500, 640, 3);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Red', 'Birch', 10, 500, 640, 3);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Yellow', 'Maple', 10, 1000, 1400, 4);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Purple', 'Maple', 10, 1000, 1400, 4);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Red', 'Maple', 10, 4000, 5000, 5);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Black', 'Maple', 10, 4000, 5000, 5);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Blue', 'Birch', 10, 250, 350, 6);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Green', 'Birch', 10, 250, 350, 6);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Orange', 'Birch', 10, 500, 800, 7);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Yellow', 'Birch', 10, 500, 800, 7);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Blue', 'Maple', 10, 1500, 2000, 8);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Red', 'Maple', 10, 1500, 2000, 8);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id)VALUES ('Purple', 'Birch', 10, 300, 350, 9);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id)VALUES ('Brown', 'Birch', 10, 300, 350, 9);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Black', 'Birch', 10, 900, 1200, 10);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES ('Yellow', 'Birch', 10, 900, 1200, 10);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id)VALUES ('Natural Wood', 'Maple', 10, 2000, 2700, 11);
INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id)VALUES ('Blue Oyster', 'Maple', 10, 2000, 2700, 11);

