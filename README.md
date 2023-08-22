# AirBnB Clone Project - Database Storage

This repository contains the implementation of a database storage system for an AirBnB clone application. The database storage is designed to manage various objects, such as users, places, amenities, and reviews, using SQLAlchemy as the Object-Relational Mapping (ORM) tool. The project aims to create a seamless and efficient storage system for the application's data.

## Table of Contents

- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Models](#models)
- [Relationships](#relationships)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.6 or higher
- SQLAlchemy
- MySQL server (or compatible database server)

## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your database connection configuration in `config.py`.

## Usage

To utilize the database storage system, follow these steps:

1. Ensure that the required packages are installed and the database configuration is set up.
2. Import the necessary classes from the `models` package to create, update, and manage your objects.

## Models

The database storage system includes the following models:

- `BaseModel`: Base class for other classes, containing common attributes and methods.
- `User`: Represents a user with attributes such as email, password, first name, and last name.
- `Place`: Represents a place with attributes like city ID, user ID, amenities, and other details.
- `Amenity`: Represents an amenity that can be associated with places.
- `Review`: Represents a review for a place, including text, user ID, and place ID.

## Relationships

- **User - Place**: A one-to-many relationship where a user can have multiple places.
- **User - Review**: A one-to-many relationship where a user can have multiple reviews.
- **Place - Amenity**: A many-to-many relationship where a place can have multiple amenities and an amenity can be associated with multiple places.
- **Place - Review**: A one-to-many relationship where a place can have multiple reviews.

## Example Usage

```python
from models import User, Place, Amenity, Review

# Create a new user
user = User(email="example@example.com", password="securepwd", first_name="John", last_name="Doe")
user.save()

# Create a new place and associate it with a user
place = Place(user_id=user.id, city_id="city123", name="Cozy Cabin")
place.save()

# Add an amenity to a place
amenity = Amenity(name="Wifi")
amenity.save()
place.amenities.append(amenity)

# Create a review for a place
review = Review(user_id=user.id, place_id=place.id, text="Amazing stay!")
review.save()

