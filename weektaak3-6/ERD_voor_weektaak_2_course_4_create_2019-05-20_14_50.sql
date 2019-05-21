-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-05-20 12:05:10.222

-- tables
-- Table: BLAST_result
CREATE TABLE BLAST_result (
    Query_id varchar(20) NOT NULL,
    resultaat_id int NOT NULL,
    acessiecode varchar(20) NOT NULL,
    e_value int NOT NULL,
    percentage_identity int NOT NULL,
    total_covery int NOT NULL,
    query_covery int NOT NULL,
    max_scores int NOT NULL,
    blast_alg_id int NOT NULL,
    sequentie varchar(600) NOT NULL,
    Grondorganisme_type varchar(25) NOT NULL,
    BLAST_settings_blast_setting_id int NOT NULL,
    Eiwit_seq_id_eiwit varchar(20) NOT NULL,
    CONSTRAINT BLAST_result_pk PRIMARY KEY (Query_id)
);

-- Table: BLAST_settings
CREATE TABLE BLAST_settings (
    blast_setting_id int NOT NULL,
    gebruikte_database varchar(5) NOT NULL,
    alg_naam varchar(7) NOT NULL,
    scorematrix varchar(20) NOT NULL,
    CONSTRAINT BLAST_settings_pk PRIMARY KEY (blast_setting_id)
);

-- Table: Eiwit
CREATE TABLE Eiwit (
    seq_id_eiwit varchar(20) NOT NULL,
    CONSTRAINT Eiwit_pk PRIMARY KEY (seq_id_eiwit)
);

-- Table: Familienaam
CREATE TABLE Familienaam (
    familienaam varchar(25) NOT NULL,
    CONSTRAINT Familienaam_pk PRIMARY KEY (familienaam)
);

-- Table: Functie_eiwit
CREATE TABLE Functie_eiwit (
    functie varchar(50) NOT NULL,
    Eiwit_seq_id_eiwit varchar(20) NOT NULL
);

-- Table: Geslachtsnaam
CREATE TABLE Geslachtsnaam (
    geslachtsnaam varchar(25) NOT NULL,
    Familienaam_familienaam varchar(25) NOT NULL,
    CONSTRAINT Geslachtsnaam_pk PRIMARY KEY (geslachtsnaam)
);

-- Table: Grondorganisme
CREATE TABLE Grondorganisme (
    type varchar(25) NOT NULL,
    Geslachtsnaam_geslachtsnaam varchar(25) NOT NULL,
    CONSTRAINT Grondorganisme_pk PRIMARY KEY (type)
);

-- foreign keys
-- Reference: BLAST_result_BLAST_settings (table: BLAST_result)
ALTER TABLE BLAST_result ADD CONSTRAINT BLAST_result_BLAST_settings FOREIGN KEY BLAST_result_BLAST_settings (BLAST_settings_blast_setting_id)
    REFERENCES BLAST_settings (blast_setting_id);

-- Reference: BLAST_result_Eiwit (table: BLAST_result)
ALTER TABLE BLAST_result ADD CONSTRAINT BLAST_result_Eiwit FOREIGN KEY BLAST_result_Eiwit (Eiwit_seq_id_eiwit)
    REFERENCES Eiwit (seq_id_eiwit);

-- Reference: BLAST_result_Grondorganisme (table: BLAST_result)
ALTER TABLE BLAST_result ADD CONSTRAINT BLAST_result_Grondorganisme FOREIGN KEY BLAST_result_Grondorganisme (Grondorganisme_type)
    REFERENCES Grondorganisme (type);

-- Reference: Functie_eiwit_Eiwit (table: Functie_eiwit)
ALTER TABLE Functie_eiwit ADD CONSTRAINT Functie_eiwit_Eiwit FOREIGN KEY Functie_eiwit_Eiwit (Eiwit_seq_id_eiwit)
    REFERENCES Eiwit (seq_id_eiwit);

-- Reference: Geslachtsnaam_Familienaam (table: Geslachtsnaam)
ALTER TABLE Geslachtsnaam ADD CONSTRAINT Geslachtsnaam_Familienaam FOREIGN KEY Geslachtsnaam_Familienaam (Familienaam_familienaam)
    REFERENCES Familienaam (familienaam);

-- Reference: Grondorganisme_Geslachtsnaam (table: Grondorganisme)
ALTER TABLE Grondorganisme ADD CONSTRAINT Grondorganisme_Geslachtsnaam FOREIGN KEY Grondorganisme_Geslachtsnaam (Geslachtsnaam_geslachtsnaam)
    REFERENCES Geslachtsnaam (geslachtsnaam);

-- End of file.

