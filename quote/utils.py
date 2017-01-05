import csv
import os
from quote.dashboard.models import Category, Product, Duration, Circulation, \
    ImageSize, ImageLocation


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        for key in kwargs:
            if kwargs[key] == '':
                instance = None
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


def save_categories(db):
    items = [
        Category(name='License'),
        Category(name='Digital Media', parent_id=1),
        Category(
            name='Digital Advertisement',
            description='Advertisement within an application, website, game or other software. Includes banner ads, over-page, in-page or web video advertisements. Use of advertisement on social media platforms requires purchase of separate "Web-Social Media" license.',
            parent_id=2
        ),
        Category(
            name='Corporate and promotional site',
            description='Commercial or promotional use on a website, including as a design element on a corporate website or in branding/profile designs on Social Media. (Does not include paid advertising; for example, "Web -- advertisement.")',
            parent_id=2
        ),
        Category(
            name='Email Marketing',
            description='A brochure distributed only via electronic means such as a download from a website or emailed upon request to customers and promotional email sent directly to individuals. Use of brochure on social media platforms requires purchase of separate "Web-Social Media" license.',
            parent_id=2
        )
    ]
    for item in items:
        db.session.add(item)
    db.session.commit()


def reset_db(db):
    db.drop_all()
    db.create_all()
