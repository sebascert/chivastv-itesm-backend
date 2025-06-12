create table if not exists comentario
(
    ID                 int auto_increment,
    usuario_email      varchar(255) null,
    video_ruta_archivo varchar(255) null,
    fecha              datetime     not null,
    contenido          text         null,
    es_en_vivo         tinyint(1)   null,
    moderado           tinyint(1)   null,
    primary key (ID, fecha),
    constraint comentario_ibfk_1
        foreign key (usuario_email) references usuario (email),
    constraint comentario_ibfk_2
        foreign key (video_ruta_archivo) references video (ruta_archivo),
    INDEX idx_usuario_email(usuario_email),
    INDEX idx_video_ruta_archivo(video_ruta_archivo)
);
