from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "metric" (
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "id" VARCHAR(27) NOT NULL  PRIMARY KEY,
    "service_name" VARCHAR(255) NOT NULL,
    "path" VARCHAR(255) NOT NULL,
    "response_time_ms" INT NOT NULL
);
CREATE INDEX IF NOT EXISTS "idx_metric_path_6047b7" ON "metric" ("path");;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "metric";"""
