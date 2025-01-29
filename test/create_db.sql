CREATE TABLE IF NOT EXISTS xm_data_hourly_per_agent (
    value FLOAT,
    record_timestamp TIMESTAMP UNIQUE
);

CREATE TABLE IF NOT EXISTS records (
    id_record INTEGER PRIMARY KEY,
    id_service INTEGER NOT NULL,
    record_timestamp TIMESTAMP NOT NULL,
    FOREIGN KEY (record_timestamp) REFERENCES xm_data_hourly_per_agent (record_timestamp)
);

CREATE TABLE IF NOT EXISTS services (
    id_service INTEGER NOT NULL,
    id_market INTEGER NOT NULL,
    cdi INTEGER NOT NULL,
    voltage_level INTEGER NOT NULL,
    PRIMARY KEY (id_service),
    UNIQUE (id_market, cdi, voltage_level)
);

CREATE TABLE IF NOT EXISTS injection (
    id_record INTEGER PRIMARY KEY,
    value FLOAT,
    FOREIGN KEY (id_record) REFERENCES records (id_record)
);

CREATE TABLE IF NOT EXISTS consumption (
    id_record INTEGER PRIMARY KEY,
    value FLOAT,
    FOREIGN KEY (id_record) REFERENCES records (id_record)
);

CREATE TABLE IF NOT EXISTS tariffs (
    id_market INTEGER NOT NULL,
    cdi INTEGER NOT NULL,
    voltage_level INTEGER NOT NULL,
    g FLOAT,
    t FLOAT,
    d FLOAT,
    r FLOAT,
    c FLOAT,
    p FLOAT,
    cu FLOAT,
    PRIMARY KEY (id_market, cdi, voltage_level),
    FOREIGN KEY (id_market, cdi, voltage_level) REFERENCES services (id_market, cdi, voltage_level)
);