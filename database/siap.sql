DROP DATABASE IF EXISTS db_siap;
CREATE DATABASE db_siap;

\c db_siap;

CREATE TABLE IF NOT EXISTS asatidz (
    asatidz_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    gender VARCHAR(1) NOT NULL,
    entry_year VARCHAR(5) NOT NULL,
    telephone_number VARCHAR(13) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(162) NOT NULL,
    pas_photo VARCHAR(50),
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS job (
    job_id SERIAL PRIMARY KEY,
    job VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS job_asatiz (
    jobaz_id SERIAL PRIMARY KEY,
    year VARCHAR(10) NOT NULL,
    asatidz_id INT REFERENCES asatidz(asatidz_id),
    job_id INT REFERENCES job(job_id)
);

CREATE TABLE IF NOT EXISTS santri (
    santri_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    address VARCHAR(255) NOT NULL,
    place_of_birth VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    entry_year VARCHAR(5) NOT NULL,
    gender VARCHAR(1) NOT NULL,
    parent_name VARCHAR(50) NOT NULL,
    telephone_number VARCHAR(13) NOT NULL,
    email VARCHAR(50) NOT NULL,
    pas_photo VARCHAR(50),
    password VARCHAR(162) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS lembaga (
    lembaga_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    alias VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS subjects (
    subjects_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    lembaga_id INT REFERENCES lembaga(lembaga_id)
);

CREATE TABLE IF NOT EXISTS mengajar (
    mengajar_id SERIAL PRIMARY KEY,
    asatidz_id INT REFERENCES asatidz(asatidz_id),
    subjects_id INT REFERENCES subjects(subjects_id)
);

CREATE TABLE IF NOT EXISTS class (
    class_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    year VARCHAR(10) NOT NULL,
    lembaga_id INT REFERENCES lembaga(lembaga_id)
);

CREATE TABLE IF NOT EXISTS mengajar_class (
    mengajar_id INT REFERENCES mengajar(mengajar_id),
    class_id INT REFERENCES class(class_id),
    PRIMARY KEY (mengajar_id, class_id)
);

CREATE TABLE IF NOT EXISTS santri_class (
    santri_class_id SERIAL PRIMARY KEY,
    santri_scores INT NOT NULL DEFAULT 0,
    santri_id INT REFERENCES santri(santri_id),
    class_id INT REFERENCES class(class_id)
);

CREATE TABLE IF NOT EXISTS absensi (
    absensi_id SERIAL PRIMARY KEY,
    is_present BOOLEAN NOT NULL DEFAULT FALSE,
    date DATE NOT NULL DEFAULT CURRENT_DATE,
    ket VARCHAR(10),
    santri_class_id INT REFERENCES santri_class(santri_class_id)
);

CREATE TABLE IF NOT EXISTS spp (
    spp_id SERIAL PRIMARY KEY,
    year VARCHAR(10) NOT NULL,
    month VARCHAR(10) NOT NULL,
    nominal INT NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS spp_santri (
    santri_id INT REFERENCES santri(santri_id),
    spp_id INT REFERENCES spp(spp_id),
    date DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (santri_id, spp_id)
);

CREATE TABLE IF NOT EXISTS takziran (
    takziran_id SERIAL PRIMARY KEY,
    pelanggaran VARCHAR(30) NOT NULL,
    nominal INT NOT NULL DEFAULT 0,
    date DATE NOT NULL DEFAULT CURRENT_DATE,
    is_lunas BOOLEAN NOT NULL DEFAULT FALSE,
    payment_date DATE,
    santri_id INT REFERENCES santri(santri_id)
);