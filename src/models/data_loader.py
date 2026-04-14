import kagglehub
from kagglehub import KaggleDatasetAdapter

# Caminho do arquivo, notar que tem um espaço entre ATS _CAL
file_path = "CAL/CAL_ATS _SOL_01_100.csv" 

try:
    print("Conectando à NASA (via Kaggle)...")
    
    # Carregando com a função atualizada
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "nikitamanaenkov/meda-mars-weather-and-atmosphere-sensor-data",
        file_path,
        # Limite para testes rápidos de desenvolvimento
        sql_query="SELECT * FROM index LIMIT 1000"
    )

    print("Sucesso! Telemetria recebida.")
    print("\nPrimeiros registros de Temperatura (ATS):")
    # Imprime as primeiras linhas e colunas essenciais
    print(df.head())

except Exception as e:
    print(f"Erro ao carregar os dados: {e}")