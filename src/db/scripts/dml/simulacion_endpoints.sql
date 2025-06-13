
-- Simulación de Endpoints tipo ChivasTV
-- =====================================

-- GET /comment/{video_id}/{start}/{end}
CALL obtener_comentarios_en_rango('video123.mp4', 0, 10);

-- POST /comment/{video_id}
CALL insertar_comentario('usuario@correo.com', 'video123.mp4', '¡Buen partido!', 0);

-- DELETE /comment/{comment_id}
CALL eliminar_comentario(5);

-- DELETE /mod/comment (moderación)
UPDATE comentario SET moderado = 1 WHERE ID = 5;

-- GET /statistics/{video_id}
CALL obtener_estadisticas('video123.mp4');

-- GET /user/
SELECT * FROM usuario WHERE email = 'usuario@correo.com';

-- DELETE /user/
DELETE FROM sesion WHERE usuario_email = 'usuario@correo.com';
DELETE FROM usuario WHERE email = 'usuario@correo.com';

-- POST /user/register/
CALL registrar_usuario('nuevo@correo.com', 'hash123', 'Ana', 'Torres');

-- POST /user/token/
CALL login_usuario('usuario@correo.com', 'hash123');

-- DELETE /user/token
DELETE FROM sesion WHERE token = 'tokenXYZ';

-- GET /video/{video_id}
CALL obtener_video(3);

-- POST /video/{video_id}/ (crear video)
CALL crear_video(
    'video456.mp4',
    'Final América vs Chivas',
    'Fútbol',
    1, 0, 1
);

-- DELETE /video/{video_id}/
UPDATE video SET deleted = 1 WHERE ID = 3;

-- PUT /video/{video_id}/
UPDATE video
SET titulo = 'Final Re-editada', descripcion = 'Versión extendida'
WHERE ID = 3;

-- GET /video/{category}
SELECT * FROM videos_por_categoria WHERE categoria_nombre = 'Fútbol';

-- GET / (root)
SELECT 'Backend activo' AS estado;
