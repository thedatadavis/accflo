import os
import shutil

import click

# --- Constants ---
# This defines the relative path to your templates directory.
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")


# --- Main CLI Group ---
# This is the main entry point defined in your pyproject.toml (`acc = "accflo.cli:cli"`)
@click.group()
def cli():
    """
    Accflo: Accounting as Code for Modern SaaS.

    This is the main CLI for managing your accounting workflows,
    from ingestion to month-end close.
    """
    pass


# --- `acc init` ---
@cli.command()
def init():
    """
    Initialize a new Accflo project.

    This creates the core configuration files in your current directory.
    """
    click.echo("Initializing new Accflo project...")

    # Files to be copied from the `templates` directory
    files_to_copy = [
        "config.yml.template",
        "dbt_project.yml.template",
    ]

    # Example: Copying config files into the user's CWD
    for file_name in files_to_copy:
        source_path = os.path.join(TEMPLATE_DIR, file_name)
        dest_path = os.path.join(os.getcwd(), file_name.replace(".template", ""))

        if os.path.exists(dest_path):
            click.echo(f"  » Skipping, '{dest_path}' already exists.")
        else:
            try:
                shutil.copy(source_path, dest_path)
                click.echo(f"  » Created '{dest_path}'")
            except FileNotFoundError:
                click.echo(
                    f"  » [Error] Template file '{source_path}' not found.", err=True
                )

    # Example: Creating directories
    dirs_to_create = ["models", "rules", "tests"]
    for dir_name in dirs_to_create:
        dest_path = os.path.join(os.getcwd(), dir_name)
        if os.path.exists(dest_path):
            click.echo(f"  » Skipping, directory '{dest_path}' already exists.")
        else:
            os.makedirs(dest_path)
            click.echo(f"  » Created directory '{dest_path}/'")

    click.echo("\n✅ Project initialized. Next steps:")
    click.echo("1. Edit 'config.yml' to connect your data sources.")
    click.echo("2. Add your business logic to the 'models/' and 'rules/' directories.")


# --- `acc ingest` ---
@cli.command()
@click.option("--source", help="Run ingestion for a specific source (e.g., 'stripe').")
def ingest(source):
    """
    Run ingestion pipelines (via dlt) to load data.
    """
    if source:
        click.echo(f"Ingesting data from source: {source}...")
    else:
        click.echo("Ingesting data from all configured sources...")
    # TODO: Add dlt pipeline logic here
    click.echo("Ingestion complete.")


# --- `acc transform` ---
@cli.command()
def transform():
    """
    Build the subledger and revenue waterfalls.
    """
    click.echo("Running transformations (Polars + DuckDB)...")
    # TODO: Add Polars/DuckDB transformation logic here
    click.echo("Subledger build complete.")


# --- `acc reconcile` (aliased as `test`) ---
@cli.command(name="test")
def reconcile():
    """
    Run reconciliation tests and assertions.
    """
    click.echo("Running reconciliation tests...")
    # TODO: Add testing/assertion logic here
    click.echo("All tests passed.")


# --- `acc close` ---
@cli.command()
@click.option(
    "--period", required=True, help="The period to close (e.g., '2025-10-31')."
)
def close(period):
    """
    Run the controlled month-end close workflow.
    """
    click.echo(f"Running close for period: {period}...")
    # TODO: Add close orchestration logic here
    click.echo("Close complete.")


# --- `acc export-audit` ---
@cli.command(name="export-audit")
@click.option(
    "--period", required=True, help="The period to export (e.g., '2025-10-31')."
)
def export_audit(period):
    """
    Export a deterministic audit bundle for a closed period.
    """
    click.echo(f"Exporting audit bundle for period: {period}...")
    # TODO: Add audit bundle generation logic here
    click.echo(f"Audit bundle saved to 'audit_{period}.zip'")


# --- `acc je ...` (Command Group) ---
@cli.group()
def je():
    """
    Manage Journal Entries (JE).
    """
    pass


@je.command(name="preview")
@click.option("--period", required=True, help="The period to preview JEs for.")
def je_preview(period):
    """
    Preview journal entries without posting.
    """
    click.echo(f"Generating JE preview for {period}...")
    # TODO: Add JE generation logic
    click.echo("--- JE Preview ---")
    click.echo("Account        | Debit  | Credit")
    click.echo("----------------|--------|-------")
    click.echo("1000-Cash      | 100.00 |       ")
    click.echo("4000-Revenue   |        | 100.00")
    click.echo("----------------|--------|-------")


@je.command(name="post")
@click.option("--period", required=True, help="The period to post JEs for.")
def je_post(period):
    """
    Post journal entries to the configured ERP.
    """
    click.echo(f"Posting JEs for {period} to ERP...")
    # TODO: Add ERP connection and posting logic
    click.echo("JEs posted successfully.")


# --- Main entry point for debugging ---
if __name__ == "__main__":
    cli()
