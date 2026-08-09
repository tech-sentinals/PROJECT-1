CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(120) NOT NULL,
    category VARCHAR(80) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    unit_price DECIMAL(10,2) NOT NULL CHECK (unit_price >= 0),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_products_category ON products(category);

INSERT INTO products(product_id, product_name, category, quantity, unit_price) VALUES
(1, 'Laptop Stand', 'Accessories', 35, 1499.00),
(2, 'Wireless Mouse', 'Accessories', 80, 799.00),
(3, 'USB-C Hub', 'Electronics', 42, 1899.00);

-- Low-stock monitoring
SELECT * FROM products WHERE quantity < 20 ORDER BY quantity;

-- Inventory value
SELECT SUM(quantity * unit_price) AS inventory_value FROM products;
