import requests

def consulta_ip(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        resposta = requests.get(url)
        dados = resposta.json()

        cidade = dados.get("city", "Não disponível")
        regiao = dados.get("region", "Não disponível")
        org = dados.get("org", "Não disponível")
        hostname = dados.get("hostname", "Não disponível")

        print(f"Cidade: {cidade}")
        print(f"Região: {regiao}")
        print(f"Organização: {org}")
        print(f"Hostname: {hostname}")

    except Exception as e:
        print(f"Erro ao consultar IP: {e}")

def main():
    ip = input("Digite o IP para consulta: ").strip()
    consulta_ip(ip)

if __name__ == "__main__":
    main()
