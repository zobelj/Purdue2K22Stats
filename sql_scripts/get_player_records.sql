select Name, sum(PF > PA) as W, sum(PF < PA) as L, round(sum(PF > PA) / count(Name), 2) as 'Win Percentage' from user_gamelogs
join players using(PlayerID)
group by PlayerID
order by W desc;

