create database IPL_Analytics;
use IPL_Analytics;


CREATE TABLE IPL_Matches
(
    id INT PRIMARY KEY,
    season VARCHAR(20),
    city VARCHAR(100),
    match_date DATE,
    team1 VARCHAR(100),
    team2 VARCHAR(100),
    toss_winner VARCHAR(100),
    toss_decision VARCHAR(20),
    result VARCHAR(50),
    dl_applied BIT,
    winner VARCHAR(100),
    win_by_runs INT,
    win_by_wickets INT,
    player_of_match VARCHAR(100),
    venue VARCHAR(200),
    umpire1 VARCHAR(100),
    umpire2 VARCHAR(100),
    umpire3 VARCHAR(100)
);

select * from IPL_Matches;

insert into IPL_Matches
SELECT * from matches_imp;

select TOP 10 * from IPL_Matches

SELECT COUNT(*) AS TOTAL_MACHTES
FROM IPL_Matches

SELECT COUNT(DISTINCT season) AS TOTAL_SEASONS
FROM IPL_Matches

SELECT DISTINCT season 
FROM IPL_Matches
ORDER BY season

SELECT DISTINCT city 
FROM IPL_Matches
ORDER BY city

SELECT DISTINCT venue 
FROM IPL_Matches
ORDER BY venue


select id ,
count(*) as duplicate_count
from IPL_Matches
group by id having count(*)>1;

select count(*) as total_matches
from IPL_Matches

select count(distinct team1) as total_teams
from IPL_Matches


select count(distinct venue) as total_venues
from IPL_Matches


select count(distinct city) as total_cities
from IPL_Matches


select winner,
count(*) as total_wins
from IPL_Matches
group by winner
order by total_wins desc

select top 10 player_of_match,
count(*) as awards
from IPL_Matches
group by player_of_match
order by awards desc

select venue,
count(*) as match_played
from IPL_Matches
group by venue
order by match_played desc

SELECT toss_decision,
COUNT(*) AS Matches
FROM IPL_Matches
GROUP BY toss_decision;


SELECT COUNT(*) AS Toss_Helped_Win
FROM IPL_Matches
WHERE toss_winner = winner;


SELECT COUNT(*) AS Won_By_Runs
FROM IPL_Matches
WHERE win_by_runs > 0;


SELECT COUNT(*) AS Won_By_Wickets
FROM IPL_Matches
WHERE win_by_wickets > 0;


SELECT TOP 1 winner,
win_by_runs
FROM IPL_Matches
ORDER BY win_by_runs DESC;


SELECT TOP 1 winner,
win_by_wickets
FROM IPL_Matches
ORDER BY win_by_wickets DESC;


SELECT city,
COUNT(*) AS Matches
FROM IPL_Matches
GROUP BY city
ORDER BY Matches DESC;
 

SELECT toss_winner,
COUNT(*) AS Toss_Wins
FROM IPL_Matches
GROUP BY toss_winner
ORDER BY Toss_Wins DESC;


 SELECT winner,
COUNT(*) * 100.0 /
(SELECT COUNT(*) FROM IPL_Matches) AS Win_Percentage
FROM IPL_Matches
GROUP BY winner
ORDER BY Win_Percentage DESC;
