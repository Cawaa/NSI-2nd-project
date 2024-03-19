-- TABLE
CREATE TABLE Calendrier
(idCalendrier INT PRIMARY KEY NOT NULL,
 titre DEFAULT (255),
 description DEFAULT (255),
 event_date DATE DEFAULT(255));

CREATE TABLE Utilisateur
(idUtilisateur INT PRIMARY KEY NOT NULL,
 prenom DEFAULT(100),
 nom DEFAULT(100),
 email DEFAULT(255),
 mot de passe DEFAULT(255));

SELECT titre
FROM Calendrier
INNER JOIN Utilisateur ON idCalendrier = idUtilisateur

CREATE TABLE populationtotale (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  gender TEXT NOT NULL
);
-- insert some values
INSERT INTO populationtotale VALUES (1, "POPULATION EN ÂGE DE TRAVAILLER ", "POPULATION DE MOINS DE 15 ANS");
INSERT INTO populationtotale VALUES (2, 'POPULATION ACTIVE               ', 'POPULATION INACTIVE');
INSERT INTO populationtotale VALUES (3, 'POPULATION ACTIVE OCCUPEE       ', 'RETRAITES, ETUDIANTS');
-- fetch some values
SELECT * FROM populationtotale WHERE gender = "POPULATION DE MOINS DE 15 ANS";
SELECT * FROM populationtotale WHERE gender = 'POPULATION INACTIVE';
SELECT * FROM populationtotale WHERE gender = 'RETRAITES, ETUDIANTS';
-- INDEX
 
-- TRIGGER
 
-- VIEW
 
