create table if not exists categoria
(
    ID          int auto_increment
        primary key,
    nombre      varchar(100) not null,
    descripcion text         null,
    constraint nombre
        unique (nombre)
);