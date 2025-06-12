create table if not exists estadisticas_partido
(
    video_ruta_archivo varchar(255) not null
        primary key,
    equipoA_nombre     varchar(100) null,
    equipoB_nombre     varchar(100) null,
    golesA             int          null,
    golesB             int          null,
    constraint estadisticas_partido_ibfk_1
        foreign key (video_ruta_archivo) references video (ruta_archivo),
    constraint estadisticas_partido_ibfk_2
        foreign key (equipoA_nombre) references equipo (nombre),
    constraint estadisticas_partido_ibfk_3
        foreign key (equipoB_nombre) references equipo (nombre),
    INDEX idx_equipoA_nombre(equipoA_nombre),
    INDEX idx_equipoB_nombre(equipoB_nombre)
);
