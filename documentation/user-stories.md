# User Stories

Käyttäjille mahdolliset toiminnot ja niiden kyselyt:
- Käyttäjänä haluan pystyä luomaan seuran jonka johtajana toimin
  - SELECT * FROM Club WHERE Club.id = X;
- Seuran johtajana haluan pystyä poistamaan seuran jäseniä
  - DELETE FROM Members M WHERE M.club_id = X AND M.user_id = Y;
- Seuran johtajana haluan pystyä lisäämään ja poistamaan ilmoituksia
  - INSERT INTO Message (club_id, message) VALUES (X, Y);
  - DELETE FROM Message M WHERE M.id = Y;
- Käyttäjänä haluan pystyä liittymään ja poistumaan seuroista, jotta pidän seuralistani ajantasalla
  - INSERT INTO Members (club_id, account_id) VALUES (X, Y);
  - DELETE FROM Members M WHERE M.club_id = X AND M.account_id = Y;
- Käyttäjänä haluan nähdä listan seuroista että voin tarkastella niitä
  - SELECT * FROM Clubs;
- Käyttäjänä haluan pystyä lisäämään itselleni harrastusvälineitä, jotta minä ja muut näkisivät mitä minulla on
  - INSERT INTO Equipment (user_id, name) VALUES (X, Y);
- Käyttäjänä haluan pystyä poistamaan itseltäni harrastusvälineitä joita minulla ei enää ole
  - DELETE FROM Equipment WHERE id = Y;
- Käyttäjänä haluan nähdä kaikki harrastusälineet jotka minulla on
  - SELECT * FROM Equipment E WHERE E.user_id = X;
- Käyttäjänä haluan nähdä muiden harrastusälineet
  - SELECT * FROM Equipment E WHERE E.user_id = X;
- Käyttäjänä haluan pystyä näkemään listan muista käyttäjistä
  - SELECT * FROM Account;
- Käyttäjänä haluan pystyä seuraamaan muita käyttäjiä, jotta pystyisin katsomaan heidän tietojaan helpommin
  - INSERT INTO Follower_table (follower_id, followed_id) VALUES (X, Y);
- Käyttäjänä haluan pystyä lopettamaan käyttäjän seuraamisen
  - DELETE FROM Follower_table WHERE follower_id = X AND followed_id = Y;
