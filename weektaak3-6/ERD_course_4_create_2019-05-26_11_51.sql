-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-05-25 21:17:50.571

-- tables
-- Table: BLAST_result
CREATE TABLE BLAST_result (
    resultaat_id int NOT NULL AUTO_INCREMENT,
    acessiecode varchar(20) NULL,
    e_value int NULL,
    percentage_identity int NULL,
    total_covery int NULL,
    query_covery int NULL,
    max_scores int NULL,
    sequentie text NOT NULL,
    Grondorganisme_type varchar(25) NULL,
    BLAST_settings_setting_id int NOT NULL,
    Eiwit_seq_id_eiwit varchar(20) NULL,
    CONSTRAINT BLAST_result_pk PRIMARY KEY (resultaat_id)
);

-- Table: BLAST_settings
CREATE TABLE BLAST_settings (
    setting_id int NOT NULL,
    gebruikte_database varchar(5) NULL,
    alg_naam varchar(7) NULL,
    scorematrix varchar(20) NULL,
    CONSTRAINT BLAST_settings_pk PRIMARY KEY (setting_id)
);

-- Table: Eiwit
CREATE TABLE Eiwit (
    eiwit_id varchar(20) NOT NULL,
    naam varchar(100) NULL,
    Functie_id int NULL,
    CONSTRAINT Eiwit_pk PRIMARY KEY (eiwit_id)
);

-- Table: Familienaam
CREATE TABLE Familienaam (
    familienaam varchar(125) NOT NULL,
    CONSTRAINT Familienaam_pk PRIMARY KEY (familienaam)
);

-- Table: Functie
CREATE TABLE Functie (
    id int NOT NULL,
    functie text NULL,
    CONSTRAINT Functie_pk PRIMARY KEY (id)
);

-- Table: Geslachtsnaam
CREATE TABLE Geslachtsnaam (
    geslachtsnaam varchar(125) NOT NULL,
    Familienaam_familienaam varchar(125) NULL,
    CONSTRAINT Geslachtsnaam_pk PRIMARY KEY (geslachtsnaam)
);

-- Table: Grondorganisme
CREATE TABLE Grondorganisme (
    type varchar(125) NOT NULL,
    Geslachtsnaam_geslachtsnaam varchar(125) NULL,
    CONSTRAINT Grondorganisme_pk PRIMARY KEY (type)
);

-- foreign keys
-- Reference: BLAST_result_BLAST_settings (table: BLAST_result)
ALTER TABLE BLAST_result ADD CONSTRAINT BLAST_result_BLAST_settings FOREIGN KEY BLAST_result_BLAST_settings (BLAST_settings_setting_id)
    REFERENCES BLAST_settings (setting_id);

-- Reference: BLAST_result_Eiwit (table: BLAST_result)
ALTER TABLE BLAST_result ADD CONSTRAINT BLAST_result_Eiwit FOREIGN KEY BLAST_result_Eiwit (Eiwit_seq_id_eiwit)
    REFERENCES Eiwit (eiwit_id);

-- Reference: BLAST_result_Grondorganisme (table: BLAST_result)
ALTER TABLE BLAST_result ADD CONSTRAINT BLAST_result_Grondorganisme FOREIGN KEY BLAST_result_Grondorganisme (Grondorganisme_type)
    REFERENCES Grondorganisme (type);

-- Reference: Eiwit_Functie (table: Eiwit)
ALTER TABLE Eiwit ADD CONSTRAINT Eiwit_Functie FOREIGN KEY Eiwit_Functie (Functie_id)
    REFERENCES Functie (id);

-- Reference: Geslachtsnaam_Familienaam (table: Geslachtsnaam)
ALTER TABLE Geslachtsnaam ADD CONSTRAINT Geslachtsnaam_Familienaam FOREIGN KEY Geslachtsnaam_Familienaam (Familienaam_familienaam)
    REFERENCES Familienaam (familienaam);

-- Reference: Grondorganisme_Geslachtsnaam (table: Grondorganisme)
ALTER TABLE Grondorganisme ADD CONSTRAINT Grondorganisme_Geslachtsnaam FOREIGN KEY Grondorganisme_Geslachtsnaam (Geslachtsnaam_geslachtsnaam)
    REFERENCES Geslachtsnaam (geslachtsnaam);

-- End of file.

