DROP TABLE IF EXISTS relocation CASCADE;

CREATE table relocation (
primary_state VARCHAR(20),
secondary_state VARCHAR,
inflow INTEGER,
outflow INTEGER,
PRIMARY KEY ("primary_state", "secondary_state"));

SELECT * from relocation;