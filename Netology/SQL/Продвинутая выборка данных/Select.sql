select g.name, count(a.name) from genre g 
left join genres_artist ga  on g.id = ga.genre_id 
left join artist a on ga.artist_id = a.id 
group by g.name 
order by count(a.id) desc

select t.name, a.year
from album a 
left join track t on t.album_id = a.id 
where (a.year >= 2019) and (a.year <= 2020) 

select a.name, avg(t.duration) from album a 
left join track t on t.album_id = a.id 
group by a.name
order by avg(t.duration)

select distinct a.name
from artist a 
where a.name not in (
	select distinct a.name
	from artist a2
	left join artist_album aa on a.id = aa.artist_id
	left join album a on a.id = aa.album_id
	where a.year = 2020
)
order by a.name

select distinct c.name
from collection c 
left join track_collection tc on c.id = tc.collection_id 
left join track t on t.id = tc.track_id
left join album a on a.id = t.album_id 
left join artist_album aa on aa.album_id = a.id 
left join artist ar on ar.id = aa.artist_id
where ar.name ilike '%Eminem'
order by c."name" 

select a.name
from album a 
left join artist_album aa on a.id  = aa.album_id 
left join artist ar on a.id = aa.artist_id 
left join genres_artist ga on a.id = ga.artist_id 
left join genre g on g.id = ga.genre_id 
group by a.name
having count(distinct g.name) > 1
order by a.name

select t.name
from track t 
left join track_collection tc on t.id = tc.track_id 
where tc.track_id is null

select a.name, t.duration
from track t 
left join album a on a.id = t.album_id 
left join artist_album aa on aa.album_id = a.id
left join artist ar on ar.id = aa.artist_id
group by a.name, t.duration 
having t.duration = (select min(duration) from track)
order by a.name

select distinct a.name
from album a 
left join track t on t.album_id = a.id 
where t.album_id in (
	select album_id
	from track 
	group by album_id
	having count(id) = (
		select count(id)
		from track 
		group by album_id
		order by count
		limit 1 
	)
)
order by a."name" 