erDiagram

    %% === ENTIDADES PRINCIPALES ===
    USUARIO {
        int id PK
        string email
        string password_hash
        string nombre
        string apellido
        string direccion
        string ciudad
        string codigo_postal
        string estado
        string pais
        string genero
        date fecha_nacimiento
        string ocupacion
        datetime fecha_creacion
    }

    PERMISO {
        int id PK
        string nombre
    }

    PERMISO_USUARIO {
        int usuario_id FK
        int permiso_id FK
    }

    SESION {
        int id PK
        int usuario_id FK
        string token
        datetime creado_en
        datetime expira_en
    }

    PAGO_PREMIUM {
        int id PK
        int usuario_id FK
        datetime fecha_pago
        string metodo
        float monto
        bool fue_exitoso
        string referencia_pasarela
    }

    VIDEO {
        int id PK
        string titulo
        string descripcion
        string ruta_archivo
        datetime fecha_subida
        int categoria_id FK
        bool es_publico
        bool es_premium
        bool es_partido
    }

    CATEGORIA {
        int id PK
        string nombre
        string descripcion
    }

    COMENTARIO {
        int id PK
        int usuario_id FK
        int video_id FK
        string contenido
        datetime fecha
        bool es_en_vivo
        bool moderado
        bool eliminado
    }

    MODERACION_COMENTARIO {
        int id PK
        int usuario_id FK
        int comentario_id FK
        string accion
        datetime fecha
    }

    LIKE_DISLIKE {
        int id PK
        int usuario_id FK
        int video_id FK
        bool es_like
    }

    VISTA_VIDEO {
        int id PK
        int video_id FK
        int usuario_id FK
        datetime fecha
        int duracion_reproducida
    }

    ESTADISTICAS_PARTIDO {
        int id PK
        int video_id FK
        int equipoA_id FK
        int equipoB_id FK
        int golesA
        int golesB
    }

    FALTA {
        int id PK
        int estadisticas_partido_id FK
        int equipo_id FK
        string descripcion
    }

    EQUIPO {
        int id PK
        string nombre
    }

    %% === RELACIONES ===
    USUARIO ||--o{ SESION : inicia
    USUARIO ||--o{ PAGO_PREMIUM : realiza
    USUARIO ||--o{ COMENTARIO : escribe
    USUARIO ||--o{ LIKE_DISLIKE : reacciona
    USUARIO ||--o{ MODERACION_COMENTARIO : modera
    USUARIO ||--o{ PERMISO_USUARIO : tiene
    USUARIO ||--o{ VISTA_VIDEO : ve

    PERMISO ||--o{ PERMISO_USUARIO : otorga

    VIDEO ||--o{ COMENTARIO : recibe
    VIDEO ||--o{ LIKE_DISLIKE : recibe
    VIDEO ||--o{ VISTA_VIDEO : es_visto
    VIDEO ||--|| ESTADISTICAS_PARTIDO : contiene

    CATEGORIA ||--o{ VIDEO : clasifica

    COMENTARIO ||--o{ MODERACION_COMENTARIO : recibe

    ESTADISTICAS_PARTIDO ||--o{ FALTA : contiene
    FALTA }o--|| EQUIPO : cometida_por

    ESTADISTICAS_PARTIDO }|--|| EQUIPO : equipoA
    ESTADISTICAS_PARTIDO }|--|| EQUIPO : equipoB

    %% === NOTAS DE PERMISOS ===
    %% Usuarios con permiso "ver_video_premium" pueden ver videos premium
    %% Usuarios con permiso "moderar_comentarios" pueden moderar comentarios
    %% El permiso "admin" implica acceso total
