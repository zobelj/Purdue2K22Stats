create table user_gamelogs(
GameID int,
TeamID ENUM ('Ballerz', 'Ringers'),
UserID varchar(20),
PF tinyint,
PA tinyint,
PlayerID tinyint,
TeammateID tinyint,
OppPlayer1 tinyint,
OppPlayer2 tinyint);

create table players(
PlayerID tinyint,
Name varchar(40));

insert into players(PlayerID, Name) values
(0, 'Mason Gillis'),
(1, 'Brian Waddell'),
(2, 'Eric Hunter Jr.'),
(3, 'Caleb Furst'),
(4, 'Trey Kaufman-Renn'),
(5, 'Brandon Newman'),
(11, 'Isaiah Thompson'),
(15, 'Zach Edey'),
(23, 'Jaden Ivey'),
(25, 'Ethan Mortan'),
(50, 'Trevion Williams'),
(55, 'Sasha Stefanovic');