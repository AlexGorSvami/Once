create table if not exists genre(
	id serial not null,
	name varchar(40) not null,
	constraint genre_pk primary key (id)
);

create table if not exists artist(
	id serial not null,
	name varchar(40) not null,
	constraint atist_pk primary key (id)
);

create table if not exists genres_artist(
	genre_id integer not null,
	artist_id integer not null,
	constraint genre_artist_fk foreign key(genre_id) references genre(id),
	constraint genre_artists_fk1 foreign key (artist_id) references artist(id)
);

create table if not exists album(
	id serial not null,
	name varchar(40) not null,
	year integer not null,
	constraint album_pk primary key (id)
);

create table if not exists artist_album(
	artist_id integer not null,
	album_id integer not null,
	constraint artist_album_fk foreign key (album_id) references album(id),
	constraint artist_album_fk1 foreign key (artist_id) references artist(id)
);


create table if not exists track(
	id serial not null,
	name varchar(40) not null,
	album_id integer not null,
	duration integer second not null,
	constraint track_pk primary key (id),
	constraint track_fk foreign key (album_id) references album (id)
);

create table if not exists collection(
	id serial not null,
	name varchar(40) not null,
	year integer not null,
	constraint collection_pk primary key (id)
);

create table if not exists track_collection(
	track_id int not null,
	collection_id int not null,
	constraint track1_collection_pk primary key (track_id, collection_id),
	constraint track1_collection_fk foreign key (collection_id) references collection (id),
	constraint track_collection_fk foreign key (track_id) references track (id)
);

insert into genre(id,name)
values 
	(1, 'Classic'),
    (2, 'Pop'),
	(3, 'Rock'),
	(4, 'Rap'),
	(5, 'RnB')

insert into artist (name)
values 
	('Rhiana'),
	('Eminem'),
	('Mozart'),
	('Queen'),
	('Linkin Park'),
	('Sia'),
	('Grot'),
	('Usher')

insert into genres_artist (genre_id, artist_id)
values 
	(1,4),
	(2,1),
	(2,2),
	(3,5),
	(3,6),
	(4,7),
	(5,8),
	(4,3)

insert into album (name, year)
values 
	('first', 2018),
	('Lose Yourself', 2008),
	('My life', 2008)
	('My vision', 2020),
	('Chocolate', 2019),
	('Numb', 2019),
	('Best', 2010),
	('New', 2011),
	('New area', 2022)

insert into artist_album (artist_id, album_id)
values 
	(1,4),
	(2,3),
	(3,5),
	(4,2),
	(5,8),
	(6,1),
	(7,6),
	(8,7)

insert into  track (name, album_id, duration)
values 
	('Life', 2, '00:04:50'),
	('My rules', 3, '00:05:00'),
	('Numb', 6, '00:02:50'),
	('Firt', 8, '00:03:10'),
	('The Best', 1, '00:02:50'),
	('My path', 6, '00:02:40'),
	('My life', 5, '00:03:10'),
	('I think', 7, '00:04:00'),
	('Today', 4, '00:05:15'),
	('My City', 4, '00:02:30'),
	('Bad', 1, '00:04:40'),
	('Roses', 8, '00:03:30'),
	('Money', 5, '00:03:10'),
	('Lose Yourself', 2, '00:02:20'),
	('The Best', 2020),
	('Dance', 2018),
	('Disco', 2021),
	('All stars', 2018),
	('Artists', 2020),
	('Cool', 2010),
	('Bands', 2015),
	('Fresh', 2017)

insert into track_collection  (track_id, collection_id)
values 
	(3,1),
	(1,2),
	(8,4),
	(2,5),
	(6,3),
	(4,8),
	(10,7),
	(15,6),
	(14,4),
	(9,5),
	(5,1),
	(4,3),
	(13,8),
	(8,3),
	(4,4)

select name, year from album 
where year = 2018


select name, duration from track 
where duration = (select max(duration) from track)


select name, duration  from track  
where duration >= '00:03:30'

select name from collection 
where year between 2018 and 2020

select name from artist 
where name not like '% %'

select name from track
where name ilike '%my%'
