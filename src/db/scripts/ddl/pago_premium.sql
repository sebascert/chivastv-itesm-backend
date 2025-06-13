create table if not exists pago_premium
(
    referencia_pasarela varchar(100) not null
        primary key,
    usuario_email       varchar(255) null,
    fecha_pago          datetime     null,
    metodo              varchar(50)  null,
    monto               float        null,
    fue_exitoso         tinyint(1)   null,
    constraint pago_premium_ibfk_1
        foreign key (usuario_email) references usuario (email),
    INDEX idx_usuario_email (usuario_email)
);

