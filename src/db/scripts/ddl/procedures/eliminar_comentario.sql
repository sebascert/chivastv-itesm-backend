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
