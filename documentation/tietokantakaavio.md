# tietokantakaavio

<img src="https://github.com/elehtine/harrastuslista/blob/master/img/t-2.png" width="640">

Kuvassa tummennetut kentät ovat pääavaimia. Viivat kuvaavat taulujen viitteitä. Viivat ovat viiteavaimesta pääavaimeen ja 1 ja * kuvaavat yhdestä moneen suhteiden suunnan. Monesta moneen suhteet ovat muodostettu liitostaulujen avulla.

## CREATE TABLE -lauseet

CREATE TABLE account (  
	id INTEGER NOT NULL,  
	date_created DATETIME,  
	date_modified DATETIME,  
	name VARCHAR(144) NOT NULL,  
	username VARCHAR(144) NOT NULL,  
	password VARCHAR(144) NOT NULL,  
	age INTEGER,  
	gender VARCHAR(10),  
	PRIMARY KEY (id)  
)

CREATE TABLE follower_table (  
	followed_id INTEGER NOT NULL,  
	follower_id INTEGER NOT NULL,  
	PRIMARY KEY (followed_id, follower_id),  
	FOREIGN KEY(followed_id) REFERENCES account (id),  
	FOREIGN KEY(follower_id) REFERENCES account (id)  
)

CREATE TABLE club (  
	id INTEGER NOT NULL,  
	date_created DATETIME,   
	date_modified DATETIME,  
	name VARCHAR(144) NOT NULL,  
	hobby VARCHAR(144) NOT NULL,  
	leader_id INTEGER NOT NULL,  
	PRIMARY KEY (id),  
	FOREIGN KEY(leader_id) REFERENCES account (id)  
)

CREATE TABLE equipment (  
	id INTEGER NOT NULL,  
	date_created DATETIME,  
	date_modified DATETIME,  
	name VARCHAR(144) NOT NULL,  
	account_id INTEGER NOT NULL,  
	PRIMARY KEY (id),  
	FOREIGN KEY(account_id) REFERENCES account (id)  
)

CREATE TABLE members (  
	club_id INTEGER NOT NULL,  
	account_id INTEGER NOT NULL,  
	PRIMARY KEY (club_id, account_id),  
	FOREIGN KEY(club_id) REFERENCES club (id),  
	FOREIGN KEY(account_id) REFERENCES account (id)  
)

CREATE TABLE message (  
	id INTEGER NOT NULL,  
	date_created DATETIME,  
	date_modified DATETIME,  
	message VARCHAR(144) NOT NULL,  
	club_id INTEGER NOT NULL,  
	PRIMARY KEY (id),  
	FOREIGN KEY(club_id) REFERENCES club (id)  
)
