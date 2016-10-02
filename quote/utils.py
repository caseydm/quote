import csv
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
    items = []
    # open file
    with open('category1.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # look up and assign option objects
            category = Category.query.filter_by(name=row['category2']).first(),
            duration = get_or_create(db.session, Duration, name=row['duration']),
            circulation = get_or_create(db.session, Circulation, name=row['circulation']),
            image_size = get_or_create(db.session, ImageSize, name=row['image_size']),
            image_location = get_or_create(db.session, ImageLocation, name=row['image_location'])

            # create products
            items.append(
                Product(
                    category_id=category.id,
                    duration_id=duration.id,
                    circulation_id=circulation.id,
                    image_size_id=image_size.id,
                    image_location_id=image_location.id,
                    price=row['price']
                )
            )

    # save to database
    for item in items:
        db.session.add(item)
    db.session.commit()
