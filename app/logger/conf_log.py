import logging


def setup_logger():
    logging.basicConfig(
        filename='app.log',  # Plik, do którego będą zapisywane logi
        filemode='a',  # Tryb otwierania pliku (a - append)
        format='%(asctime)s - %(levelname)s - %(message)s',  # Format logów
        datefmt='%Y-%m-%d %H:%M:%S',  # Format daty i czasu
        level=logging.INFO  # Poziom logowania
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(console_handler)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)


if __name__ == "__main__":
    setup_logger()
