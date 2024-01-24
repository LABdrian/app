from scraper import CSVDownloader
from strategie import CSVTransformer

def main():
    try:

        CSVDownloader.execute()
        CSVTransformer.execute()
    except Exception as e:
        print(f"Se produjo un error durante la ejecución: {e}")

if __name__ == "__main__":
    main()