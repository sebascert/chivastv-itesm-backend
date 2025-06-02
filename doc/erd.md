
classDiagram
    
    %% === CLASE BASE ===
    class Usuario {
        +int id
        +string email
        +string password_hash
        +string nombre
        +string apellido
        +string direccion
        +string ciudad
        +string codigo_postal
        +string estado
        +string pais
        +string genero
        +date fecha_nacimiento
        +string ocupacion
        +datetime fecha_creacion
        +bool es_premium
    }

    %% === ROLES Y PERMISOS ===
    class Permiso {
        +int id
        +string nombre
    }

    class AdminUser {
        +int id
        +string email
        +string password_hash
    }

    class AdminPermiso {
        +int admin_id
        +int permiso_id
    }

    %% === MODERACIÓN ===
    class ModeracionComentario {
        +int id
        +int admin_id
        +int comentario_id
        +string accion
        +datetime fecha
    }

    %% === SESIONES Y PAGOS ===
    class Sesion {
        +int id
        +int usuario_id
        +string token
        +datetime creado_en
        +datetime expira_en
    }

    class PagoPremium {
        +int id
        +int usuario_id
        +datetime fecha_pago
        +string metodo
        +float monto
        +bool fue_exitoso
        +string referencia_pasarela
    }

    %% === VIDEO Y CATEGORÍAS ===
    class Video {
        +int id
        +string titulo
        +string descripcion
        +string ruta_archivo
        +datetime fecha_subida
        +int categoria_id
        +bool es_publico
        +bool es_premium
        +bool es_partido
    }

    class Categoria {
        +int id
        +string nombre
        +string descripcion
    }

    %% === INTERACCIONES ===
    class Comentario {
        +int id
        +int usuario_id
        +int video_id
        +string contenido
        +datetime fecha
        +bool es_en_vivo
        +bool moderado
        +bool eliminado
    }

    class LikeDislike {
        +int id
        +int usuario_id
        +int video_id
        +bool es_like
    }

    class VistaVideo {
        +int id
        +int video_id
        +datetime fecha
        +int duracion_reproducida
    }

    %% === ESTADÍSTICAS DE PARTIDO Y EQUIPO ===
    class EstadisticasPartido {
        +int id
        +int video_id
        +int equipoA_id
        +int equipoB_id
        +int golesA
        +int golesB
    }

    class Falta {
        +int id
        +int estadisticas_partido_id
        +int equipo_id
        +string descripcion
    }

    class Equipo {
        +int id
        +string nombre
    }

    %% === RELACIONES ===
    Usuario "1" --> "*" Sesion : inicia
    Usuario "1" --> "*" PagoPremium : realiza
    Usuario "1" --> "*" Comentario : escribe
    Usuario "1" --> "*" LikeDislike : reacciona
    Video "1" --> "*" VistaVideo : vistas

    AdminUser "1" --> "*" AdminPermiso : tiene
    AdminPermiso "*" --> "1" Permiso : refiere

    AdminUser "1" --> "*" ModeracionComentario : modera
    Comentario "1" --> "*" ModeracionComentario : recibe

    Categoria "1" --> "*" Video : clasifica
    Video "1" --> "*" Comentario : recibe
    Video "1" --> "*" LikeDislike : recibe
    Video "1" --> "*" VistaVideo : vistas

    Usuario "1" --> "*" Video : puede ver según es_premium

    EstadisticasPartido "1" --> "1" Equipo : equipoA
    EstadisticasPartido "1" --> "1" Equipo : equipoB
    EstadisticasPartido "1" --> "*" Falta : contiene faltas
    Falta "*" --> "1" Equipo : cometida por

    Video "1" --> "0..1" EstadisticasPartido : contiene

