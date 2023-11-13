CREATE TABLE IF NOT EXISTS produtos (
    code INT(4) UNSIGNED ZEROFILL NOT NULL,
    name CHAR(50),
    stock CHAR(50),
    value FLOAT,
    id_categoria TINYINT NULL,
    PRIMARY KEY (code)
);

CREATE TABLE IF NOT EXISTS categories (
    id TINYINT NOT NULL,
    name CHAR(40) NOT NULL,
    description VARCHAR(200),
    PRIMARY KEY (id)
);

ALTER TABLE produtos ADD FOREIGN KEY (id_categoria) REFERENCES categories(id);