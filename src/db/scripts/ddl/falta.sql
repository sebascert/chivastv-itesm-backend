create table if not exists falta
(
    video_ruta_archivo varchar(255) not null,
    equipo_nombre      varchar(100) not null,
    momento            datetime     not null,
    descripcion        text         null,
    primary key (video_ruta_archivo, equipo_nombre, momento),
    constraint falta_ibfk_1
        foreign key (video_ruta_archivo) references estadisticas_partido (video_ruta_archivo),
    constraint falta_ibfk_2
        foreign key (equipo_nombre) references equipo (nombre),
    INDEX idx_equipo_nombre(equipo_nombre)
);

