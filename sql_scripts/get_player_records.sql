select Name, sum(PF > PA) as W, sum(PF < PA) as L from user_gamelogs
join players using(PlayerID)
group by PlayerID
order by W desc;

