DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    name VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE products (
    name VARCHAR(255),
    description VARCHAR(255),
    in_stock INT,
    purchase_cost INT,
    selling_cost INT,
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE,
    id SERIAL PRIMARY KEY
);

INSERT INTO manufacturers (name) VALUES ('DW');
INSERT INTO manufacturers (name) VALUES ('Pearl');
INSERT INTO manufacturers (name) VALUES ('Mapex');
INSERT INTO manufacturers (name) VALUES ('Ludwig');


INSERT INTO products (name, description, in_stock, purchase_cost, selling_cost, manufacturer_id) VALUES ('Design', 'Intermediate', 10, 1000, 1500, 1);
INSERT INTO products (name, description, in_stock, purchase_cost, selling_cost, manufacturer_id) VALUES ('Performance', 'Pro', 10, 2000, 2500, 1);
INSERT INTO products (name, description, in_stock, purchase_cost, selling_cost, manufacturer_id) VALUES ('Export', 'Beginner', 10, 500, 640, 2);
INSERT INTO products (name, description, in_stock, purchase_cost, selling_cost, manufacturer_id) VALUES ('Masters', 'Intermediate', 10, 1000, 1400, 2);
INSERT INTO products (name, description, in_stock, purchase_cost, selling_cost, manufacturer_id) VALUES ('Masterworks', 'Pro', 10, 4000, 5000, 2);
INSERT INTO products (name, description, in_stock, purchase_cost, selling_cost, manufacturer_id) VALUES ('Tornado', 'Beginner', 10, 250, 350, 3);
INSERT INTO products (name, description, in_stock, purchase_cost, selling_cost, manufacturer_id) VALUES ('Armory', 'Intermediate', 10, 500, 800, 3);
INSERT INTO products (name, description, in_stock, purchase_cost, selling_cost, manufacturer_id) VALUES ('Saturn', 'Pro', 10, 1500, 2000, 3);
INSERT INTO products (name, description, in_stock, purchase_cost, selling_cost, manufacturer_id) VALUES ('Pocket', 'Beginner', 10, 300, 350, 4);
INSERT INTO products (name, description, in_stock, purchase_cost, selling_cost, manufacturer_id) VALUES ('NeuSonic', 'Intermediate', 10, 900, 1200, 4);
INSERT INTO products (name, description, in_stock, purchase_cost, selling_cost, manufacturer_id) VALUES ('Classic', 'Pro', 10, 2000, 2700, 4);