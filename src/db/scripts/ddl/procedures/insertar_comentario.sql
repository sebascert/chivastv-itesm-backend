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
