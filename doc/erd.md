```mermaid
erDiagram
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

    MODERACION_LOG {
        int id PK
        string accion
        datetime fecha
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
    USUARIO ||--o{ PERMISO_USUARIO : tiene

    PERMISO ||--o{ PERMISO_USUARIO : otorga

    VIDEO ||--o{ COMENTARIO : recibe
    VIDEO ||--|| ESTADISTICAS_PARTIDO : contiene

    CATEGORIA ||--o{ VIDEO : clasifica

    COMENTARIO ||--o{ MODERACION_LOG : recibe

    ESTADISTICAS_PARTIDO ||--o{ FALTA : contiene
    FALTA }o--|| EQUIPO : cometida_por

    ESTADISTICAS_PARTIDO }|--|| EQUIPO : equipoA
    ESTADISTICAS_PARTIDO }|--|| EQUIPO : equipoB

    %% === NUEVAS RELACIONES PARA ADMINISTRADORES ===
    USUARIO ||--o{ MODERACION_LOG : puede_acceder_si_admin
    USUARIO ||--o{ COMENTARIO : puede_borrar_si_admin

    %% === NOTAS DE PERMISOS ===
    %% Usuarios con permiso "ver_video_premium" pueden ver videos premium
    %% Usuarios con permiso "moderar_comentarios" pueden moderar comentarios
    %% El permiso "admin" implica acceso total, incluyendo acceso al log de moderación y eliminación de comentarios
