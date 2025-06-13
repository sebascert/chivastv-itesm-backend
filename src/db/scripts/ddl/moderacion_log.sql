create table if not exists moderacion_log
(
    ID                 int auto_increment
        primary key,
    email              varchar(255) null,
    video_ruta_archivo varchar(255) null,
    fecha              datetime     null,
    accion             text         null,
    constraint moderacion_log_ibfk_1
        foreign key (email) references usuario (email),
    constraint moderacion_log_ibfk_2
        foreign key (video_ruta_archivo) references video (ruta_archivo),
    INDEX idx_admin_email(email),
    INDEX idx_video_ruta_archivo(video_ruta_archivo)
);

