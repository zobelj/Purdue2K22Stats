#User records
select UserID, sum(PF > PA) as W, sum(PF < PA) as L, round(avg(PF),1) as PF, round(avg(PA),1) as PA from user_gamelogs
group by UserID
order by W desc;
