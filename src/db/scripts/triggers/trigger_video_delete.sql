DROP TRIGGER IF EXISTS VideoDelete;

CREATE TRIGGER VideoDelete
AFTER UPDATE ON video
FOR EACH ROW
BEGIN
    IF NEW.deleted = 1 AND OLD.deleted = 0 THEN
        UPDATE comentario
        SET moderado = 1
        WHERE video_ruta_archivo = OLD.ruta_archivo;
    END IF;
END;
