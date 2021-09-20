use health001


create table patient (
        id_patient integer NOT NULL AUTO_INCREMENT ,
        id_device    varchar(48),
        p_name varchar(32),
        PRIMARY KEY (id_patient)
);

create table dispense_medication (
        id_dm integer NOT NULL AUTO_INCREMENT,
        id_patient integer,
        m_name varchar(64),
        hour    integer,
        PRIMARY KEY (id_dm)
);

create table dispense_medication_sent (
        id_dms integer NOT NULL AUTO_INCREMENT,
        id_patient integer,
        m_name varchar(64),
        c_time  timestamp,
        status  int,
        PRIMARY KEY (id_dms)
);

create table test_heart (
        id_th integer NOT NULL AUTO_INCREMENT,
        id_patient integer,
        hour    integer,
        PRIMARY KEY (id_th)
);

create table test_heart_sent (
        id_ths integer NOT NULL AUTO_INCREMENT,
        id_patient integer,
        bpm float,
        spo2 float,
        c_time  timestamp,
        PRIMARY KEY (id_ths)
);

create table doctor_appointment (
        id_da integer NOT NULL AUTO_INCREMENT,
        id_patient integer,
        m_doctor varchar(64),
        appointment datetime,
        PRIMARY KEY (id_da)
);

