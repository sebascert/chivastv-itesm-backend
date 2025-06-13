create table if not exists usuario
(
    ID               int auto_increment
        primary key,
    email            varchar(255)                       not null,
    password_hash    varchar(255)                       not null,
    nombre           varchar(100)                       null,
    apellido         varchar(100)                       null,
    direccion        text                               null,
    ciudad           varchar(100)                       null,
    codigo_postal    varchar(20)                        null,
    estado           varchar(100)                       null,
    pais             varchar(100)                       null,
    genero           varchar(20)                        null,
    fecha_nacimiento date                               null,
    ocupacion        varchar(100)                       null,
    fecha_creacion   datetime default CURRENT_TIMESTAMP null,
    constraint email
        unique (email)
);

