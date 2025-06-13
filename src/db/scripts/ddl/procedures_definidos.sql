
-- ===========================================
-- DEFINICIÓN DE STORED PROCEDURES DEL SISTEMA
-- ===========================================

-- Obtener comentarios visibles en un rango (paginación)
DROP PROCEDURE IF EXISTS obtener_comentarios_en_rango;
DELIMITER //
CREATE PROCEDURE obtener_comentarios_en_rango(
    IN video_ruta_archivo VARCHAR(255),
    IN inicio INT,
    IN fin INT
)
BEGIN
    SELECT * FROM comentarios_visibles
    WHERE video_ruta_archivo = video_ruta_archivo
    ORDER BY fecha
    LIMIT inicio, fin;
END;
//
DELIMITER ;

-- Insertar un nuevo comentario
DROP PROCEDURE IF EXISTS insertar_comentario;
DELIMITER //
CREATE PROCEDURE insertar_comentario(
    IN usuario_email VARCHAR(255),
    IN video_ruta_archivo VARCHAR(255),
    IN contenido TEXT,
    IN es_en_vivo TINYINT
)
BEGIN
    INSERT INTO comentario (
        usuario_email,
        video_ruta_archivo,
        fecha,
        contenido,
        es_en_vivo,
        moderado
    )
    VALUES (
        usuario_email,
        video_ruta_archivo,
        NOW(),
        contenido,
        es_en_vivo,
        0
    );
END;
//
DELIMITER ;

-- Eliminar un comentario por ID
DROP PROCEDURE IF EXISTS eliminar_comentario;
DELIMITER //
CREATE PROCEDURE eliminar_comentario(
    IN ID INT
)
BEGIN
    DELETE FROM comentario WHERE ID = ID;
END;
//
DELIMITER ;

-- Obtener estadísticas + faltas de un video
DROP PROCEDURE IF EXISTS obtener_estadisticas;
DELIMITER //
CREATE PROCEDURE obtener_estadisticas(
    IN video_ruta_archivo VARCHAR(255)
)
BEGIN
    SELECT * FROM vista_estadisticas_partido
    WHERE video_ruta_archivo = video_ruta_archivo;
END;
//
DELIMITER ;

-- Registrar un nuevo usuario
DROP PROCEDURE IF EXISTS registrar_usuario;
DELIMITER //
CREATE PROCEDURE registrar_usuario(
    IN email VARCHAR(255),
    IN password_hash VARCHAR(255),
    IN nombre VARCHAR(100),
    IN apellido VARCHAR(100)
)
BEGIN
    INSERT INTO usuario (email, password_hash, nombre, apellido)
    VALUES (email, password_hash, nombre, apellido);
END;
//
DELIMITER ;

-- Login de usuario
DROP PROCEDURE IF EXISTS login_usuario;
DELIMITER //
CREATE PROCEDURE login_usuario(
    IN email VARCHAR(255),
    IN password_hash VARCHAR(255)
)
BEGIN
    SELECT ID, email FROM usuario
    WHERE email = email AND password_hash = password_hash;
END;
//
DELIMITER ;

-- Obtener información de video
DROP PROCEDURE IF EXISTS obtener_video;
DELIMITER //
CREATE PROCEDURE obtener_video(
    IN ID INT
)
BEGIN
    SELECT * FROM video WHERE ID = ID AND deleted = 0;
END;
//
DELIMITER ;

-- Crear un nuevo video
DROP PROCEDURE IF EXISTS crear_video;
DELIMITER //
CREATE PROCEDURE crear_video(
    IN ruta_archivo VARCHAR(255),
    IN titulo VARCHAR(200),
    IN categoria_nombre VARCHAR(100),
    IN es_publico TINYINT,
    IN es_premium TINYINT,
    IN es_partido TINYINT
)
BEGIN
    INSERT INTO video (
        ruta_archivo, titulo, fecha_subida, categoria_nombre,
        es_publico, es_premium, es_partido, deleted
    )
    VALUES (
        ruta_archivo, titulo, NOW(), categoria_nombre,
        es_publico, es_premium, es_partido, 0
    );
END;
//
DELIMITER ;
