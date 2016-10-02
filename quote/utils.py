import csv
import os
from quote.dashboard.models import Category, Product, Duration, Circulation, \
    ImageSize, ImageLocation


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


def save_products(db):
    # open file
    csv_file = os.path.join(os.path.dirname(__file__), 'category1.csv')
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # look up and assign option objects
            price = row['price']
            price = price.replace(',', '')
            category = Category.query.filter_by(name=row['category2']).first()
            duration = get_or_create(db.session, Duration, name=row['duration'])
            circulation = get_or_create(db.session, Circulation, name=row['circulation'])
            image_size = get_or_create(db.session, ImageSize, name=row['image_size'])
            image_location = get_or_create(db.session, ImageLocation, name=row['image_location'])

            # create product
            product = Product(
                price=price,
            )
            product.category = category
            product.duration = duration
            product.circulation = circulation
            product.image_size = image_size
            product.image_location = image_location
            # create products
            db.session.add(product)

    # save to database
    db.session.commit()
