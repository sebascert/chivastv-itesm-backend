create table if not exists permiso
(
    ID     int          not null
        primary key,
    nombre varchar(100) not null,
    constraint nombre
        unique (nombre)
);

