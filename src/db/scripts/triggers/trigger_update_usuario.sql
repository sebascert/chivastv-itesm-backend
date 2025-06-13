DROP TRIGGER IF EXISTS UpdateUsuario;

CREATE TRIGGER IF NOT EXISTS UpdateUsuario
AFTER INSERT ON pago_premium
FOR EACH ROW
BEGIN
    DECLARE user_id INT;

    IF NEW.fue_exitoso = 1 THEN
        SELECT id INTO user_id
        FROM usuario
        WHERE email = NEW.usuario_email;

        INSERT INTO permiso_usuario(usuario_id, permiso_nombre)
        VALUES (user_id, 'premium');
    END IF;
END;
