-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-05-27 11:05:48.849

-- tables
-- Table: BLAST_result
CREATE TABLE BLAST_result (
    resultaat_id int NOT NULL AUTO_INCREMENT,
    accessiecode varchar(20) NULL,
    e_value varchar(20) NULL,
    percentage_identity int NULL,
    total_coverage int NULL,
    query_coverage int NULL,
    max_scores int NULL,
    sequentie text NOT NULL,
    setting_id int NOT NULL,
    eiwit_id int NULL,
    Geslachtsnaam_id int NULL,
    CONSTRAINT BLAST_result_pk PRIMARY KEY (resultaat_id)
);

-- Table: Eiwit
CREATE TABLE Eiwit (
    id int NOT NULL,
    naam varchar(100) NULL,
    Functie_id int NULL,
    CONSTRAINT Eiwit_pk PRIMARY KEY (id)
);

-- Table: Familienaam
CREATE TABLE Familienaam (
    familienaam varchar(125) NULL,
    id int NOT NULL,
    CONSTRAINT Familienaam_pk PRIMARY KEY (id)
);

-- Table: Functie
CREATE TABLE Functie (
    id int NOT NULL,
    functie text NULL,
    CONSTRAINT Functie_pk PRIMARY KEY (id)
);

-- Table: Geslachtsnaam
CREATE TABLE Geslachtsnaam (
    geslachtsnaam varchar(125) NULL,
    id int NOT NULL,
    familie_id int NULL,
    CONSTRAINT Geslachtsnaam_pk PRIMARY KEY (id)
);

-- Table: Settings
CREATE TABLE Settings (
    id int NOT NULL,
    `database` varchar(60) NULL,
    alg_naam varchar(60) NULL,
    scorematrix varchar(60) NULL,
    CONSTRAINT Settings_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: BLAST_result_BLAST_settings (table: BLAST_result)
ALTER TABLE BLAST_result ADD CONSTRAINT BLAST_result_BLAST_settings FOREIGN KEY BLAST_result_BLAST_settings (setting_id)
    REFERENCES Settings (id);

-- Reference: BLAST_result_Eiwit (table: BLAST_result)
ALTER TABLE BLAST_result ADD CONSTRAINT BLAST_result_Eiwit FOREIGN KEY BLAST_result_Eiwit (eiwit_id)
    REFERENCES Eiwit (id);

-- Reference: BLAST_result_Geslachtsnaam (table: BLAST_result)
ALTER TABLE BLAST_result ADD CONSTRAINT BLAST_result_Geslachtsnaam FOREIGN KEY BLAST_result_Geslachtsnaam (Geslachtsnaam_id)
    REFERENCES Geslachtsnaam (id);

-- Reference: Eiwit_Functie (table: Eiwit)
ALTER TABLE Eiwit ADD CONSTRAINT Eiwit_Functie FOREIGN KEY Eiwit_Functie (Functie_id)
    REFERENCES Functie (id);

-- Reference: Geslachtsnaam_Familienaam (table: Geslachtsnaam)
ALTER TABLE Geslachtsnaam ADD CONSTRAINT Geslachtsnaam_Familienaam FOREIGN KEY Geslachtsnaam_Familienaam (familie_id)
    REFERENCES Familienaam (id);

-- End of file.

