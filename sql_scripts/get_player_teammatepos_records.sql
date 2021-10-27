select b1.Name, b2.Position as "Tmmt Pos", sum(PF > PA) as W, sum(PF < PA) as L, round(sum(PF > PA)/count(*),3) as wpct from user_gamelogs gl
join players b1 on b1.playerID = gl.playerID
join players b2 on b2.playerID = TeammateID
group by b1.PlayerID, b2.Position
;