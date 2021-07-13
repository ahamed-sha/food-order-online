CREATE TABLE IF NOT EXISTS customer (
	cust_id integer PRIMARY KEY,
	cust_name text,
	cust_phone text
);

CREATE TABLE IF NOT EXISTS restaurant (
    rest_id integer PRIMARY KEY,
    rest_name text,
    rest_phone text,
    menu
)

CREATE TABLE IF NOT EXISTS menu (
    rest_id integer PRIMARY KEY,
    menu_id integer,
    item_name text
)

CREATE TABLE IF NOT EXISTS order (
    cust_id integer,
    rest_id integer FOREIGN KEY,
    order_id integer FOREIGN KEY,
    items text,
    menu_id integer FOREIGN KEY,
    quantity integer
)
