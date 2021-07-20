DROP TABLE IF EXISTS boundaries;

CREATE TABLE boundaries (
	state_name VARCHAR,
	region INTEGER,
	geo_point_2d POINT
);

ALTER TABLE boundaries
ADD PRIMARY KEY (state_name);

SELECT * from boundaries;