from sqlalchemy.orm import registry, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import String, Integer, DateTime

# Registrador de tabelas
table_registry = registry()

@table_registry.mapped_as_dataclass
class PessoaFisica:
    __tablename__ = 'pessoa_fisica'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, init=False)
    nm_pessoa_fisica: Mapped[str] = mapped_column(String, nullable=False)
    dt_nascimento: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    ie_sexo: Mapped[str] = mapped_column(String, nullable=False)
    qt_idade: Mapped[int] = mapped_column(Integer, nullable=False)
    nr_cpf: Mapped[str] = mapped_column(String, nullable=False)
    dt_nrec: Mapped[datetime] = mapped_column(DateTime, nullable=True)

@table_registry.mapped_as_dataclass
class Usuario:
    __tablename__ = 'usuario'
    
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, init=False)
    nm_usuario: Mapped[str] = mapped_column(String, nullable=False)
    ds_senha: Mapped[str] = mapped_column(String, nullable=False)
    dt_nrec: Mapped[datetime] = mapped_column(DateTime, nullable=True)
