create table if not exists video
(
    ID               int auto_increment
        primary key,
    ruta_archivo     varchar(255)         not null,
    titulo           varchar(200)         null,
    descripcion      text                 null,
    fecha_subida     datetime             null,
    categoria_nombre varchar(100)         null,
    es_publico       tinyint(1)           null,
    es_premium       tinyint(1)           null,
    es_partido       tinyint(1)           null,
    deleted          tinyint(1) default 0 null,
    constraint ruta_archivo
        unique (ruta_archivo),
    constraint video_ibfk_1
        foreign key (categoria_nombre) references categoria (nombre),
    INDEX idx_categoria_nombre(categoria_nombre)
);

