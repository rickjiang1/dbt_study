from dagster import Definitions, ScheduleDefinition, define_asset_job
from dagster_dbt import DbtCliResource, build_dbt_asset_selection
from .assets import dbt_project_assets
from .project import dbt_project_dir


dbt_job = define_asset_job(
    name="dbt_run_all_job",
    selection="*",   # 👈 run all assets
)

staging_selection = build_dbt_asset_selection(
    [dbt_project_assets],
    dbt_select="tag:Staging",
)

staging_job = define_asset_job(
    name="staging_job",
    selection=staging_selection,
)

daily_dbt_schedule = ScheduleDefinition(
    name="daily_dbt_schedule",
    cron_schedule="55 10 * * *",
    target=dbt_job,
    execution_timezone="America/New_York",
)

defs = Definitions(
    assets=[dbt_project_assets],
      jobs=[
        dbt_job,
        staging_job,
    ],
    schedules=[daily_dbt_schedule],
    resources={
    "dbt": DbtCliResource(
        project_dir=dbt_project_dir,
        profiles_dir=r"C:\Users\JintaoJiang\.dbt",
        profile="dbt_project_study",
        target="dev",
        dbt_executable=r"C:\Users\JintaoJiang\AppData\Local\Programs\Python\Python310\Scripts\dbt.exe",   # 👈 force normal dbt CLI
    )
    },
)



