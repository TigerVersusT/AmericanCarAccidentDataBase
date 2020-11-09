
-- a table containing basic information of the accident 
create table if not exists Accident 
(
	AID char(20)  primary key,
	Source char(20),
	TMC char(5),
	Severity smallint,
	StartTime datetime,
	EndTime datetime,
	Distance float,
	Description varchar(255)
);

-- a table recording location information of an accident
create table if not exists Location
(
	LID integer not null auto_increment primary key,
	LAID char(20) not null,
	StartLat double null,
	StartLng double null,
	EndLat double null,
	EndLng double null,
	_Number char(16) null, 
	Street char(32) null,
	Side char(1)  null,
	City varchar(64) null,
	County varchar(64) null,
	_State varchar(64) null,
	Zipcode varchar(64) null,
	Country varchar(64) null,
	Timezone varchar(64) null,
	AirportCode varchar(64) null,
	
	foreign key (LAID) references Accident(AID) on delete cascade

);

-- a table containing weather information
create table if not exists WeatherCondition
(
	WID integer not null auto_increment primary key,
	WAID char(20) not null,
	WeatherTimeStamp datetime null,
	Temperature decimal(4, 1) null,
	WindChill decimal(4, 1) null,
	Humidity decimal(4, 1) null,
	Pressure decimal(4, 2) null,
	Visibility decimal(4,1) null,
	WindDirection char(16) null,
	WindSpeed decimal(4, 2) null,
	Precipitation decimal(3, 2) null,
	WeatherCondition varchar(64) null,
	
	foreign key (WAID) references Accident(AID) on delete cascade
);

-- a table containing information of nearby point-of-interst
create table if not exists PointOfInterst
(
	PID integer not null auto_increment primary key,
	PAID char(20) not null,
	Amenity char(8) null,
	Bump  char(8) null,
	Crossing char(8) null,
	GiveWay  char(8) null,
	Junction  char(8) null,
	NoExit  char(8) null,
	RailWay  char(8) null,
	RoundAbout  char(8) null,
	Station  char(8) null,
	Stop  char(8) null,
	TrafficCalmig  char(8) null,
	TrafficSignal  char(8) null,
	TurningLoop  char(8) null,
	
	foreign key (PAID) references Accident(AID) on delete cascade
);

-- a table containing twilight information
create table if not exists Twilight
(
	TID integer not null auto_increment primary key,
	TAID char(20) not null,
	SunriseSunset char(16) null,
	CivilTwilight char(16) null,
	NauticalTwilight char(16) null,
	AstronomicalTwilight char(16) null,
	
	foreign key (TAID) references Accident(AID) on delete cascade
);
