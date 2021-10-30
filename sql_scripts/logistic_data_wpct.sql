select (PF>PA) as W, player.wpct as Player, teammate.wpct as Teammate, opp1.wpct as Opp1, opp2.wpct as Opp2 from user_gamelogs
join (select PlayerID, Name, sum(PF > PA) as W, sum(PF < PA) as L, round(sum(PF > PA) / count(Name), 3) as 'wpct', 
sum((PF = 21 and PF > PA) or (PF = 22 and PA <= 19)) as regW, sum((PA = 21 and PA > PF) or (PA = 22 and PF <= 19)) as regL,
round(avg(PF),1) as PPG, round(avg(PA),1) as PAPG from user_gamelogs
join players using(PlayerID)
group by PlayerID
order by W desc) player using(PlayerID)
join (select PlayerID as TeammateID, Name, sum(PF > PA) as W, sum(PF < PA) as L, round(sum(PF > PA) / count(Name), 3) as 'wpct', 
sum((PF = 21 and PF > PA) or (PF = 22 and PA <= 19)) as regW, sum((PA = 21 and PA > PF) or (PA = 22 and PF <= 19)) as regL,
round(avg(PF),1) as PPG, round(avg(PA),1) as PAPG from user_gamelogs
join players using(PlayerID)
group by PlayerID
order by W desc) teammate using(TeammateID)
join (select PlayerID as OppPlayer1, Name, sum(PF > PA) as W, sum(PF < PA) as L, round(sum(PF > PA) / count(Name), 3) as 'wpct', 
sum((PF = 21 and PF > PA) or (PF = 22 and PA <= 19)) as regW, sum((PA = 21 and PA > PF) or (PA = 22 and PF <= 19)) as regL,
round(avg(PF),1) as PPG, round(avg(PA),1) as PAPG from user_gamelogs
join players using(PlayerID)
group by PlayerID
order by W desc) opp1 using (OppPlayer1)
join (select PlayerID as OppPlayer2, Name, sum(PF > PA) as W, sum(PF < PA) as L, round(sum(PF > PA) / count(Name), 3) as 'wpct', 
sum((PF = 21 and PF > PA) or (PF = 22 and PA <= 19)) as regW, sum((PA = 21 and PA > PF) or (PA = 22 and PF <= 19)) as regL,
round(avg(PF),1) as PPG, round(avg(PA),1) as PAPG from user_gamelogs
join players using(PlayerID)
group by PlayerID
order by W desc) opp2 using (OppPlayer2)
;