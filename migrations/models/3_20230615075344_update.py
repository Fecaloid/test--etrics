from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "idx_metric_path_6047b7";
        CREATE INDEX "idx_metric_service_023640" ON "metric" ("service_name");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "idx_metric_service_023640";
        CREATE INDEX "idx_metric_path_6047b7" ON "metric" ("path");"""
