create table if not exists permiso_usuario
(
    user_ID        int          not null,
    permiso_nombre varchar(100) not null,
    primary key (user_ID, permiso_nombre),
    constraint permiso_usuario_ibfk_2
        foreign key (permiso_nombre) references permiso (nombre),
    constraint permiso_usuario_usuario_ID_fk
        foreign key (user_ID) references usuario (ID),
    INDEX idx_permiso_nombre (permiso_nombre)
);

