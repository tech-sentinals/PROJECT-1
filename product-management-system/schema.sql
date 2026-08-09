-- Product Management System schema
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY,
    category_name VARCHAR(80) UNIQUE NOT NULL
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    category_id INTEGER NOT NULL,
    product_name VARCHAR(120) NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

INSERT INTO categories VALUES (1, 'Electronics'), (2, 'Accessories');
INSERT INTO products VALUES
(101, 1, 'Keyboard', 1299.00, 25),
(102, 2, 'Mouse', 799.00, 40);

SELECT p.product_id, p.product_name, c.category_name, p.price, p.stock
FROM products p JOIN categories c ON c.category_id = p.category_id;
