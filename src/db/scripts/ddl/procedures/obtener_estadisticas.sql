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
