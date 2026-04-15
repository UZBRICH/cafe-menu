import csv
from main.models import Product, Category

def run_import():
    print("IMPORT STARTED 🚀")

    with open('products.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            category_name = row['Gurux'].strip()

            category, _ = Category.objects.get_or_create(
                name=category_name
            )

            Product.objects.create(
                name=row['Nomi'].strip(),
                price=float(row['Narxi'].replace(',', '')),
                description=row['Tavsif'].strip(),
                category=category
            )