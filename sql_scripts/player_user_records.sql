select UserID, Name, sum(PF > PA) as W, sum(PA > PF) as L, round(sum(PF > PA)/count(*),3) as wpct from user_gamelogs 
join players using(PlayerID)
group by UserID, Name
order by W desc, wpct desc;
