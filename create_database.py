sql = """

-- Original data table:
CREATE TABLE data(timestamp, co2, temperature, deviceid);

-- Devices table
CREATE TABLE DEVICES (deviceid integer primary key, identifier text);

INSERT INTO DEVICES (deviceid, identifier) values (1, 'co2meter');

BEGIN TRANSACTION;
CREATE TABLE data_backup(timestamp, co2, temperature, deviceid);
INSERT INTO data_backup SELECT timestamp, co2, temperature, deviceid FROM data_old;
ALTER TABLE data RENAME TO data_empty;
ALTER TABLE data_backup RENAME TO data;
COMMIT;


-- New key-value table

CREATE TABLE data_multi_sensor (timestamp datetime, 
                                deviceid integer,
                                key text, 
                                value real);


INSERT INTO data_multi_sensor SELECT timestamp, deviceid, 'temperature', temperature FROM data;

INSERT INTO data_multi_sensor SELECT timestamp, deviceid, 'co2', co2 FROM data;


-- 

"""