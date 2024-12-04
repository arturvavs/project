from sqlalchemy.orm import registry, Mapped, mapped_column
from datetime import datetime, date, timezone
from sqlalchemy import  func, TIMESTAMP 

# Registrador de tabelas
table_registry = registry()

@table_registry.mapped_as_dataclass
class PessoaFisicaDB:
    __tablename__ = 'pessoa_fisica'
    
    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    nm_pessoa_fisica: Mapped[str] = mapped_column(nullable=False)
    dt_nascimento: Mapped[date] = mapped_column(nullable=False)
    ie_sexo: Mapped[str] = mapped_column(nullable=False)
    qt_idade: Mapped[int] = mapped_column(nullable=False)
    nr_cpf: Mapped[str] = mapped_column(nullable=False)
    nm_usuario: Mapped[str] = mapped_column(unique=True, nullable=False)
    ds_senha: Mapped[str] = mapped_column(nullable=False)
    dt_nrec: Mapped[datetime] = mapped_column(TIMESTAMP, init=False, nullable=False, server_default=func.now())
    dt_updated: Mapped[datetime] = mapped_column(TIMESTAMP, init=False, nullable=True,server_default=func.now(), onupdate=func.now())

@table_registry.mapped_as_dataclass
class UsuarioDB:
    __tablename__ = 'usuario'
    
    user_id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    nm_usuario: Mapped[str] = mapped_column(unique=True, nullable=False)
    ds_senha: Mapped[str] = mapped_column(nullable=False)
    dt_nrec: Mapped[datetime] = mapped_column(init=False, nullable=True, server_default=func.now())
 