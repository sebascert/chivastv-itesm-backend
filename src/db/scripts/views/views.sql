create or replace definer = root@localhost view comentarios_sin_borrar as
select`comentario`.`ID`                 AS `ID`,
      `comentario`.`usuario_email`      AS `usuario_email`,
      `comentario`.`video_ruta_archivo` AS `video_ruta_archivo`,
      `comentario`.`fecha`              AS `fecha`,
      `comentario`.`contenido`          AS `contenido`,
      `comentario`.`es_en_vivo`         AS `es_en_vivo`,
      `comentario`.`moderado`           AS `moderado`
from`comentario`
where (`comentario`.`moderado` = 0);

create or replace definer = root@localhost view non_deleted_videos as
select`video`.`ID`               AS `ID`,
      `video`.`ruta_archivo`     AS `ruta_archivo`,
      `video`.`titulo`           AS `titulo`,
      `video`.`descripcion`      AS `descripcion`,
      `video`.`fecha_subida`     AS `fecha_subida`,
      `video`.`categoria_nombre` AS `categoria_nombre`,
      `video`.`es_publico`       AS `es_publico`,
      `video`.`es_premium`       AS `es_premium`,
      `video`.`es_partido`       AS `es_partido`,
      `video`.`deleted`          AS `deleted`
from`video`
where (`video`.`deleted` = 0);

