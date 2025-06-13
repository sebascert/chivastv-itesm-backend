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
