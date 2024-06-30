import subprocess
import requests
import click

url = 'https://us-central1-gcp-book-1.cloudfunctions.net/function-2'


def token():
    proc = subprocess.Popen(
        ['C:\\Users\\sw-jr\\AppData\\Local\\Google\\Cloud SDK\\google-cloud-sdk\\bin\\gcloud', "auth", "print-identity-token"],
        stdout=subprocess.PIPE, shell=True)
    out, err = proc.communicate()
    return out.decode('utf-8').strip()


@click.command()
@click.argument('text', type=click.STRING)
def main(text):
    resp = requests.post(
            url,
            json={"message": text},
            headers={"Authorization": f"Bearer {token()}"})

    click.echo(f"{resp.text}")