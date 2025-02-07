-- configuração sqlite3
--.mode columns
--.headers on
--.nullvalue NULL

-- removendo tabelas caso necessário
DROP TABLE IF EXISTS worker;
DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS topping;
DROP TABLE IF EXISTS size;
DROP TABLE IF EXISTS pizza;
DROP TABLE IF EXISTS order_item;
DROP TABLE IF EXISTS orders;

-- criando tabelas
CREATE TABLE IF NOT EXISTS worker (
  id INTEGER PRIMARY KEY,
  name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS client (
  id INTEGER PRIMARY KEY,
  name TEXT,
  phone TEXT UNIQUE,
  address TEXT
);

CREATE TABLE IF NOT EXISTS topping (
  id INTEGER PRIMARY KEY,
  name TEXT UNIQUE,
  factor REAL
);

CREATE TABLE IF NOT EXISTS size (
  id INTEGER PRIMARY KEY,
  name TEXT UNIQUE,
  price REAL
);

CREATE TABLE IF NOT EXISTS pizza (
  id INTEGER PRIMARY KEY,
  quantity INT,
  topping_id INT REFERENCES top(id),
  size_id INT REFERENCES sizes(id)
);

CREATE TABLE IF NOT EXISTS order_item (
  order_id INT REFERENCES orders(id),
  pizza_id INT REFERENCES pizza(id),
  PRIMARY KEY (order_id, pizza_id)
);

CREATE TABLE IF NOT EXISTS orders (
  id INTEGER PRIMARY KEY,
  worker_id INT REFERENCES worker(id),
  client_id INT REFERENCES client(id)
);

-- limpando tabelas caso necessário
DELETE FROM worker;
DELETE FROM client;
DELETE FROM topping;
DELETE FROM size;
DELETE FROM pizza;
DELETE FROM order_item;
DELETE FROM orders;

-- dados fictícios
INSERT INTO worker (name) VALUES
('Mercúrio'),
('Vênus'),
('Marte'),
('Júpiter'),
('Saturno'),
('Urano'),
('Netuno');

INSERT INTO client (name, phone, address) VALUES
('Marco Aurélio', '5586988263719', 'Rua Roma, 439'),
('Cícero', '55869987078123', 'Rua Milão, 1045');

INSERT INTO topping (name, factor) VALUES
('Margherita', 1.2),
('Calabresa', 1.3),
('Quatro Queijos', 1.3),
('Portuguesa', 1.3),
('Pepperoni', 1.4),
('Abacaxi', 1.8),
('Caprese', 2.0);

INSERT INTO size (name, price) VALUES
('Pequena', 15),
('Média', 20),
('Grande', 25);
