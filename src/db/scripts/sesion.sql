create table if not exists sesion
(
    token         varchar(255) not null
        primary key,
    usuario_email varchar(255) null,
    creado_en     datetime     not null,
    expira_en     datetime     not null,
    constraint sesion_ibfk_1
        foreign key (usuario_email) references usuario (email),
    INDEX idx_usuario_email (usuario_email)
);

