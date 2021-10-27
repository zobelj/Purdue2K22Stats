#User records
select UserID, sum(PF > PA) as W, sum(PF < PA) as L, round(avg(PF),1) as PF, round(avg(PA),1) as PA from user_gamelogs
group by UserID
order by W desc;


#User combinations
select concat(u1.UserID," and ", u2.UserID) as Names, sum(u1.PF > u1.PA) as W, sum(u1.PF < u1.PA) as L from user_gamelogs u1
join user_gamelogs u2 on u1.GameID = u2.GameID and u1.TeamID = u2.TeamID and u1.UserID != u2.UserID
where u1.UserID < u2.UserID
group by u1.UserID, u2.UserID
order by W desc;


