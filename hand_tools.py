from sqlalchemy import create_engine, MetaData, Table


def __delete_revision(revision_id: str):
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
    metadata = MetaData(bind=engine)

    alembic_version_table = Table('alembic_version', metadata, autoload_with=engine)

    with engine.connect() as connection:
        delete_statement = alembic_version_table.delete().where(alembic_version_table.c.version_num == revision_id)
        connection.execute(delete_statement)

    print(f"Запись о ревизии {revision_id} удалена из таблицы alembic_version.")


__delete_revision('bbf2184487ce')
