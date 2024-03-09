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
 
-- INDEX
 
-- TRIGGER
 
-- VIEW
 
