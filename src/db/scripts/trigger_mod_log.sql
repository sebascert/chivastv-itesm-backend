DROP TRIGGER IF EXISTS ModLog;

CREATE TRIGGER ModLog
AFTER UPDATE ON comentario
FOR EACH ROW
BEGIN
    IF NEW.moderado = 1 THEN
        INSERT INTO moderacion_log(email, video_ruta_archivo, fecha, accion)
        VALUES (NEW.usuario_email, NEW.video_ruta_archivo, NEW.fecha, 'Comentario Eliminado');
    END IF;
END;