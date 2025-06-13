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
