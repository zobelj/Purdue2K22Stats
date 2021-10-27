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
Name varchar(40),
Position varchar(1));

insert into players(PlayerID, Name, Position) values
(0, 'Mason Gillis','F'),
(1, 'Brian Waddell','F'),
(2, 'Eric Hunter Jr.','G'),
(3, 'Caleb Furst','F'),
(4, 'Trey Kaufman-Renn','F'),
(5, 'Brandon Newman','G'),
(11, 'Isaiah Thompson','G'),
(15, 'Zach Edey','C'),
(23, 'Jaden Ivey','G'),
(25, 'Ethan Morton','G'),
(50, 'Trevion Williams','C'),
(55, 'Sasha Stefanovic','G');