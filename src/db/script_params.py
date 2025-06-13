from dataclasses import dataclass


@dataclass
class DBBaseScriptParams:
    """base database script parameters"""

@dataclass
class ObtenerComentariosParams(DBBaseScriptParams):
    video_ruta_archivo: str
    inicio: int
    fin: int


@dataclass
class InsertarComentarioParams(DBBaseScriptParams):
    usuario_email: str
    video_ruta_archivo: str
    contenido: str
    es_en_vivo: int


@dataclass
class EliminarComentarioParams(DBBaseScriptParams):
    ID: int


@dataclass
class ObtenerEstadisticasParams(DBBaseScriptParams):
    video_ruta_archivo: str


@dataclass
class RegistrarUsuarioParams(DBBaseScriptParams):
    email: str
    password_hash: str
    nombre: str
    apellido: str


@dataclass
class LoginUsuarioParams(DBBaseScriptParams):
    email: str
    password_hash: str


@dataclass
class CrearVideoParams(DBBaseScriptParams):
    ruta_archivo: str
    titulo: str
    categoria_nombre: str
    es_publico: int
    es_premium: int
    es_partido: int


@dataclass
class ObtenerVideoParams(DBBaseScriptParams):
    ID: int

