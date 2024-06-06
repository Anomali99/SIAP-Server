INSERT INTO job (job) VALUES ('Admin'), ('Administrasi'), ('Keamanan');

--password 1234
INSERT INTO asatidz (name, gender, entry_year, telephone_number, password, is_active, email) VALUES (
    'admin', '-', '0000', '1234', 'scrypt:32768:8:1$0rYWhQoKnhjMuFLZ$fe15270945daf1b6e7e732b6a9e5d38eaffdf9d4a781fe4efe3c90066fb9931c722e4276647510bc8e4824c8f1e6a53b5d4e95653ffd05f01c23bbbc44d40f6a', TRUE, 'admin'
);

INSERT INTO job_asatiz (year, asatidz_id, job_id) VALUES (
    '0000-0000', 1, 1
);