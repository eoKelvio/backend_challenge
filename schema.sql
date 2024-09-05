CREATE TABLE persons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(30) UNIQUE NOT NULL,
    gender VARCHAR(10),
    birth_date DATE NOT NULL,
    address VARCHAR NOT NULL,
    salary FLOAT NOT NULL,
    cpf VARCHAR(11) NOT NULL
);

CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    status_id INTEGER NOT NULL,
    due_day INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    balance FLOAT NOT NULL,
    avaliable_balance FLOAT NOT NULL,
    CONSTRAINT fk_person
        FOREIGN KEY(person_id) 
        REFERENCES persons(id)
);

CREATE TABLE cards (
    id SERIAL PRIMARY KEY,
    card_number VARCHAR(16) NOT NULL,
    account_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    limit FLOAT NOT NULL,
    expiration_date VARCHAR NOT NULL,
    CONSTRAINT fk_account
        FOREIGN KEY(account_id) 
        REFERENCES accounts(id)
);
