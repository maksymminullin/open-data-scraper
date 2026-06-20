import argparse
import csv
from pathlib import Path


def get_all_csv_files(base_directory: str | Path) -> list[Path]:

    folder = Path(base_directory)

    files = list(folder.rglob("*.csv"))

    return files


def main():
    parser = argparse.ArgumentParser(
        description="A script to find CSV files containing vocabulary words."
    )

    parser.add_argument(
        "folder_path",
        type=str,
        help="Path to the folder containing CSV files (e.g., /mnt/d/my_words",
    )

    args = parser.parse_args()

    target_folder = args.folder_path

    print(f"🔍 Searching for files in: {target_folder}...\n")

    found_files = get_all_csv_files(target_folder)

    if not found_files:
        print("❌ No CSV files found. Please check the provided path!")
    else:
        print(f"✅ Found {len(found_files)} file(s):")
        for file_path in found_files:
            print(f"📁 {file_path.parent.name} -> 📄 {file_path.name}")


if __name__ == "__main__":
    main()
