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