# harrastuslista

Aineopintojen harjoitustyö: tietokantasovellus -kurssia varten tehty tietokantasovellus. 

## käyttöohjeet
Käyttöohjeet löytyvät tiedostosta [käyttöohje](https://github.com/elehtine/harrastuslista/blob/master/documentation/k%C3%A4ytt%C3%B6ohje.md).

## Aihekuvaus

Sovelluksella pystytään pitämään kirjaa harrastusseuroista. Käyttäjät voivat tehdä oman seuran jonka johtajana hän toimii. Muut käyttäjät voivat liittyä seuraan. Seuran johtaja voi halutessaan poistaa käyttäjän seurastaan ja tehdä ilmoituksia seuraan liittyen. Jokaisella käyttäjällä on oma lista omistamistaan harrastusvälineistä, jota he voivat hallita itse. Käyttäjät voivat lisätä toisiaan kavereiksi niin he näkevät helpommin toistensa tiedot.
Tietokantakaavio on tiedostossa [tietokantakaavio](https://github.com/elehtine/harrastuslista/blob/master/documentation/tietokantakaavio.md).

## User Storyt

User storyt ovat tiedostossa [user-stories](https://github.com/elehtine/harrastuslista/blob/master/documentation/user-stories.md).

## Heroku

Projektin voi avata Herokussa osoitteesta [harrastuslista.herokuapp.com](https://harrastuslista.herokuapp.com/)

## Käyttäjät

Sovellukseen voi luoda käyttäjiä. Sovelluksessa on vain yksi käyttäjärooli. Käyttäjä voi lisätä itselleen harrastusvälineitä ja luoda seuran jonka johtajana käyttäjä toimii.

## Asennusohjeet
Voit käyttää ohjelmaa herokun kautta. Voit ladata projektin myös omalle koneellesi. Kun projektikansio on koneellasi ja olet komentorivillä kyseisessä kansiossa, luo Python-virtuaaliympäristö komennolla `python3 -m venv venv`. Nyt saat asennettua riippuvuudet projektiin komennolla `pip install -r requirements.txt`. Nyt sovelluksen pitäisi käynnistyä komennolla `python3 run.py`.

Kun avaat projektin seuraavan kerran sinun pitää vain aktivoida Python-virtuaaliympäristö oikesta kansiosta komennolla `source venv/bin/activate` ja voit käynnistää sovelluksen taas komennolla `python3 run.py`.
