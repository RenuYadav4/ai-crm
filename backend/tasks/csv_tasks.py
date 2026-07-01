import csv


def process_csv(file_path: str):
    print("=" * 50)
    print(f"Processing file: {file_path}")

    total_rows = 0

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_rows += 1

            print(
                f"Row {total_rows}: "
                f"{row['name']} | "
                f"{row['email']} | "
                f"{row['company']}"
            )

    print("-" * 50)
    print(f"Total Rows Processed: {total_rows}")
    print("=" * 50)

    return {
        "status": "success",
        "rows_processed": total_rows
    }