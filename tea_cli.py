import click
import requests

TEA_API_URL = "https://api.tea.xyz"  # Здесь должна быть реальная API

@click.group()
def cli():
    """Простая CLI-утилита для работы с TEA"""
    pass

@click.command()
@click.argument("wallet")
def balance(wallet):
    """Проверить баланс кошелька TEA"""
    try:
        response = requests.get(f"{TEA_API_URL}/balance/{wallet}", timeout=10)
        response.raise_for_status()
        data = response.json()
        click.echo(f"Баланс: {data.get('balance', 'Неизвестно')} TEA")
    except requests.exceptions.RequestException as e:
        click.echo(f"Ошибка при получении баланса: {e}")
    except Exception as e:
        click.echo(f"Непредвиденная ошибка: {e}")

cli.add_command(balance)

if __name__ == "__main__":
    try:
        cli()
    except SystemExit as e:
        if e.code != 0:
            raise