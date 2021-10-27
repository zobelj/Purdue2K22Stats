select Name, sum(PF > PA) as W, sum(PF < PA) as L, round(sum(PF > PA) / count(Name), 3) as 'wpct', 
sum((PF = 21 and PF > PA) or (PF = 22 and PA <= 19)) as regW, sum((PA = 21 and PA > PF) or (PA = 22 and PF <= 19)) as regL from user_gamelogs
join players using(PlayerID)
group by PlayerID
order by W desc;