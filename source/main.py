import argparse
from config.config import Config


def main() -> None:
    parser = argparse.ArgumentParser(description="znrt is nostr relay testsiute.")
    parser.add_argument("config_file", type=str, help="path to the json configuration file.")
    args = parser.parse_args()

    cfg = Config(args.config_file)
    try:
        cfg.load()
        print("configuration loaded successfully:")
        print(cfg)
    except Exception as e:
        print(f"failed to load configuration: {e}")


if __name__ == "__main__":
    main()
