
-- === USUARIOS ===
INSERT INTO USUARIO (ID, email, password_hash, nombre, apellido, direccion, ciudad, codigo_postal, estado, pais, genero, fecha_nacimiento, ocupacion)
VALUES
(1, 'admin@example.com', 'hash_admin', 'Ana', 'Admin', 'Calle 1', 'CiudadX', '12345', 'EstadoX', 'PaisY', 'Femenino', '1980-01-01', 'Administrador'),
(2, 'premium@example.com', 'hash_premium', 'Pedro', 'Premium', 'Calle 2', 'CiudadY', '23456', 'EstadoY', 'PaisY', 'Masculino', '1990-06-15', 'Ingeniero'),
(3, 'free@example.com', 'hash_free', 'Fabiola', 'Free', 'Calle 3', 'CiudadZ', '34567', 'EstadoZ', 'PaisY', 'Femenino', '2000-03-10', 'Estudiante');

-- === PERMISOS ===
INSERT INTO PERMISO (ID, nombre)
VALUES
(1, 'admin'),
(2, 'premium'),
(3, 'free');

-- === PERMISOS DE USUARIOS ===
INSERT INTO PERMISO_USUARIO (user_ID, permiso_nombre)
VALUES
(1, 'admin'),
(2, 'premium'),
(3, 'free');

-- === SESIONES ===
INSERT INTO SESION (token, usuario_email, creado_en, expira_en)
VALUES
('token_admin', 'admin@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP + INTERVAL 1 DAY),
('token_premium', 'premium@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP + INTERVAL 1 DAY),
('token_free', 'free@example.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP + INTERVAL 1 DAY);

-- === PAGOS PREMIUM ===
INSERT INTO PAGO_PREMIUM (referencia_pasarela, usuario_email, fecha_pago, metodo, monto, fue_exitoso)
VALUES
('pago123', 'premium@example.com', CURRENT_TIMESTAMP, 'Tarjeta', 12.99, TRUE);

-- === CATEGORÍAS ACTUALIZADAS ===
INSERT INTO CATEGORIA (ID, nombre, descripcion) VALUES
(1, 'Clásico De México', 'Contenido de la sección'),
(2, 'Santuario Rojiblanco', 'Contenido de la sección'),
(3, 'Raíces', 'Contenido de la sección'),
(4, 'Detrás Del Rebaño', 'Contenido de la sección'),
(5, 'Resumen', 'Contenido de la sección'),
(6, 'Repeticiones', 'Contenido de la sección'),
(7, 'Resiliencia', 'Contenido de la sección'),
(8, 'Chivas Femenil', 'Contenido de la sección'),
(9, 'Chivas Varonil', 'Contenido de la sección'),
(10, 'Sub\'s', 'Contenido de la sección'),
(11, 'Entrevistas', 'Contenido de la sección'),
(12, 'Día A Día Rojiblanco', 'Contenido de la sección'),
(13, 'Highlights On Field', 'Contenido de la sección'),
(14, 'Leyendas', 'Contenido de la sección'),
(15, 'Historia Sagrada', 'Contenido de la sección'),
(16, 'Nación Chivas', 'Contenido de la sección'),
(17, 'Operación Valorant', 'Contenido de la sección'),
(18, 'Esports', 'Contenido de la sección'),
(19, 'El Podcast De Las Chivas', 'Contenido de la sección'),
(20, 'El Recuerdo', 'Contenido de la sección');

-- === VIDEOS ===
INSERT INTO VIDEO (ID, ruta_archivo, titulo, descripcion, fecha_subida, categoria_nombre, es_publico, es_premium, es_partido)
VALUES
-- Público y partido
(1, 'videos/partido_publico.mp4', 'Partido Abierto A vs B', 'Accesible para todos', CURRENT_TIMESTAMP, 'Clásico De México', TRUE, FALSE, TRUE),
-- Solo premium
(2, 'videos/premium1.mp4', 'Documental Premium', 'Solo usuarios premium', CURRENT_TIMESTAMP, 'Resiliencia', FALSE, TRUE, FALSE),
-- Público pero no partido
(3, 'videos/highlight1.mp4', 'Resumen de goles', 'Destacado de la semana', CURRENT_TIMESTAMP, 'Resumen', TRUE, FALSE, FALSE);

-- === COMENTARIOS ===
INSERT INTO COMENTARIO (ID, usuario_email, video_ruta_archivo, fecha, contenido, es_en_vivo, moderado, eliminado)
VALUES
(1, 'premium@example.com', 'videos/partido_publico.mp4', CURRENT_TIMESTAMP, 'Buen partido!', FALSE, FALSE, FALSE),
(2, 'free@example.com', 'videos/highlight1.mp4', CURRENT_TIMESTAMP, 'Gran gol!', FALSE, FALSE, FALSE);

-- === MODERACIÓN ===
INSERT INTO MODERACION_LOG (ID, admin_email, video_ruta_archivo, comentario_fecha, fecha, accion)
VALUES
(1, 'admin@example.com', 'videos/highlight1.mp4',
    (SELECT fecha FROM COMENTARIO WHERE ID = 2),
    CURRENT_TIMESTAMP, 'Comentario marcado como ofensivo');

-- === EQUIPOS ===
INSERT INTO EQUIPO (nombre)
VALUES
('Equipo A'), ('Equipo B');

-- === ESTADÍSTICAS DE PARTIDO ===
INSERT INTO ESTADISTICAS_PARTIDO (video_ruta_archivo, equipoA_nombre, equipoB_nombre, golesA, golesB)
VALUES
('videos/partido_publico.mp4', 'Equipo A', 'Equipo B', 3, 2);

-- === FALTAS ===
INSERT INTO FALTA (video_ruta_archivo, equipo_nombre, momento, descripcion)
VALUES
('videos/partido_publico.mp4', 'Equipo A', CURRENT_TIMESTAMP - INTERVAL 30 MINUTE, 'Falta leve en el área chica');
