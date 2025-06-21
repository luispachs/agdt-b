CREATE TYPE tax_type AS ENUM('FIXED','PERCENTUAL');

CREATE TABLE users(
id BIGINT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
name VARCHAR(100) NOT NULL,
lastname VARCHAR(100) NOT NULL,
phone VARCHAR(20) NOT NULL UNIQUE,
email VARCHAR(20) NOT NULL UNIQUE,
password VARCHAR(256) NOT NULL,
address VARCHAR(150) NOT NULL UNIQUE,
isChild BOOLEAN DEFAULT false,
parent BIGINT,
FOREIGN KEY (parent) REFERENCES users(id)
);

CREATE TABLE planes(
id BIGINT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
name VARCHAR(100) NOT NULL,
monthly FLOAT NOT NULL  DEFAULT 0.0,
yearly FLOAT NOT NULL DEFAULT 0.0,
head_square_number INT DEFAULT 1
);

INSERT INTO planes(name,monthly,yearly,head_square_number)
VALUES('FREE',0.0,0.0,1),('STARTER',9.99,109.0,3),('BUSINESS',19.99,216.0,10);

CREATE TABLE business(
id BIGINT NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
name VARCHAR(160) NOT NULL,
business_addres VARCHAR(160) NOT NULL UNIQUE,
business_phone VARCHAR(20) NOT NULL UNIQUE,
owner_id BIGINT NOT NULL
);
CREATE TABLE business_plan(
id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
plan_id BIGINT NOT NULL,
business_id BIGINT NOT NULL,
FOREIGN KEY (plan_id) REFERENCES planes(id),
FOREIGN KEY (business_id) REFERENCES business(id)
);

CREATE TABLE permissions (
id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
business_id BIGINT NOT NULL,
can_create_user BOOLEAN DEFAULT false,
can_edit_user BOOLEAN DEFAULT false,
can_delete_user BOOLEAN DEFAULT false,
can_create_service BOOLEAN DEFAULT false,
can_edit_service BOOLEAN DEFAULT false,
can_delete_service BOOLEAN DEFAULT false,
can_create_modification BOOLEAN DEFAULT false,
can_edit_modification BOOLEAN DEFAULT false,
can_delete_modification BOOLEAN DEFAULT false,
can_generate_modification BOOLEAN DEFAULT false,
can_look_service BOOLEAN DEFAULT false,
FOREIGN KEY (business_id) REFERENCES business(id)
);

CREATE TABLE roles(
id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
name VARCHAR(100) NOT NULL,
permission_id BIGINT NOT NULL,
FOREIGN KEY (permission_id) REFERENCES permissions(id)
);


CREATE TABLE tax(
id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
name VARCHAR(300) NOT NULL,
value FLOAT NOT NULL DEFAULT 0.0,
type tax_type NOT NULL DEFAULT 'FIXED',
business_id BIGINT NOT NULL,
FOREIGN KEY (business_id) REFERENCES business(id)
);

CREATE TABLE services(
id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
name VARCHAR(100) NOT NULL,
service_value FLOAT NOT NULL DEFAULT 0.0,
description TEXT,
business_id BIGINT NOT NULL,
FOREIGN KEY (business_id) REFERENCES business(id)
);

CREATE TABLE modifications(
id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
name VARCHAR(100) NOT NULL,
price FLOAT NOT NULL DEFAULT 0.0,
business_id BIGINT NOT NULL,
FOREIGN KEY (business_id) REFERENCES business(id)
);

CREATE TABLE services_tax(
id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
services_id BIGINT NOT NULL,
tax_id BIGINT NOT NULL,
FOREIGN KEY (services_id) REFERENCES services(id),
FOREIGN KEY (tax_id) REFERENCES tax(id)
);

CREATE TABLE modifications_services(
id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
services_id BIGINT NOT NULL,
modification_id BIGINT NOT NULL,
FOREIGN KEY(services_id) REFERENCES services(id),
FOREIGN KEY (modification_id) REFERENCES modifications(id)
);

CREATE TYPE payment_frecuency_type AS ENUM('MONTHLY','YEARLY');

ALTER TABLE business
ADD COLUMN payment_frequency payment_frecuency_type DEFAULT NULL,
ADD COLUMN start_services DATE DEFAULT NULL;