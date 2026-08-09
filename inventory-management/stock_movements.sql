-- Inventory Management System
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    role VARCHAR(30) NOT NULL CHECK (role IN ('admin','manager','staff'))
);

CREATE TABLE stock_movements (
    movement_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    movement_type VARCHAR(10) NOT NULL CHECK (movement_type IN ('IN','OUT')),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    movement_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
