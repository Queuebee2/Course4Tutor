-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-05-27 11:05:48.849

-- foreign keys
ALTER TABLE BLAST_result
    DROP FOREIGN KEY BLAST_result_BLAST_settings;

ALTER TABLE BLAST_result
    DROP FOREIGN KEY BLAST_result_Eiwit;

ALTER TABLE BLAST_result
    DROP FOREIGN KEY BLAST_result_Geslachtsnaam;

ALTER TABLE Eiwit
    DROP FOREIGN KEY Eiwit_Functie;

ALTER TABLE Geslachtsnaam
    DROP FOREIGN KEY Geslachtsnaam_Familienaam;

-- tables
DROP TABLE BLAST_result;

DROP TABLE Eiwit;

DROP TABLE Familienaam;

DROP TABLE Functie;

DROP TABLE Geslachtsnaam;

DROP TABLE Settings;

-- End of file.

