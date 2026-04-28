from pathlib import Path

dagster_project_dir = Path(__file__).resolve().parent
dbt_project_dir = dagster_project_dir.parent.parent
dbt_manifest_path = dbt_project_dir / "target" / "manifest.json"