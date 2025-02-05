DELETE FROM worker;
DELETE FROM client;
DELETE FROM top;
DELETE FROM sizes;
DELETE FROM pizza;
DELETE FROM orders;

INSERT INTO worker (name) VALUES
('Mercúrio'),
('Vênus'),
('Marte'),
('Júpiter'),
('Saturno'),
('Urano'),
('Netuno');

INSERT INTO top (name, factor) VALUES
('Margherita', 1.2),
('Calabresa', 1.3),
('Quatro Queijos', 1.3),
('Portuguesa', 1.3),
('Pepperoni', 1.4),
('Abacaxi', 1.8),
('Caprese', 2.0);

INSERT INTO sizes (name, price) VALUES
('Pequena', 15),
('Média', 20),
('Grande', 25);
