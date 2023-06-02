# FireSale

FireSale is a Django project developed in a hands on CS course
at Reykjavík University, called Verklegt Námskeið 2.
The project is a web application resembling CraigsList in functionality.
The authors are Bríet Eva, Eyþór Mikael, Rannveig Birta and Sara Atladóttir, Engineering and CS students at RU.

Below are instructions for setting up and running the project, and
a list of requirements that were used to develop the project, respectively

## Setup

To run this project on your machine you need Python version 3.9 or higher,
credentials to a Google Storages Bucket and credentials to an SQL database.
Below is a code snippet demonstrating setting up the project on a Linux or MacOS machine.

```bash
# Clone the repo using SSH or HTTP (SSH shown here)
git clone git@github.com:mikaeleythor/firesale.git

# Enter the repository root directory
cd firesale

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the required packages
python3 -m pip install -r src/requirements.txt
```

Now that all requirements have been met you will need to provide the following
files containing your credentials:

- `.gs_key.json` which contains credentials to your Google Storage Bucket
- `.env` which contains the key-value pairs listed in the snippet below

```
GS_BUCKET_NAME=<name of your bucket>
GS_FILE=<name of your .gs_key.json file if you want to name it differently>
DB_ENGINE=<e.g. django.db.backends.postgresql_psycopg2 for PostgreSQL>
DB_NAME=<name of your database>
DB_USER=<name of your database user>
DB_HOST=<host of your database e.g. an IP address>
DB_PORT=<port on your host where db is listening, e.g. 5432 for PostgreSQL>
DB_PASSWORD=<db user password>
SECRET=<django secret key>
```

## Running the project

Below are instructions for running the project for the first time
```bash
# Enter the src/ directory
cd src

# Make initial migrations on your empty database
python3 manage.py makemigrations {person,item,notifications}
python3 manage.py migrate

# Create a superuser for access to the admin site
python3 manage.py createsuperuser

# Run the server using Django's default WSGI implementation
python3 manage.py runserver
```




## Requirement lists

The following requirement lists were developed in tandem with
a requirement analysis report, aimed to streamline the development process.
The requirements are categorized by priority A, B and C, where
A contains absolutely necessary features, B contains important features
and C contains features that are nice and make sense but could be skipped.

#### Requirements A

- [x] It should be possible to register as a new user.
- [x] It should be possible to login when a user has a registered account.
- [x] It should be possible to view your own profile.
- [x] Users should be able to view a profile picture.
- [x] Users should be able to view an average rating.
- [x] User should be able to view Full name.
- [x] User should be able to view their bio.
- [x] Users should be able to edit a profile picture.
- [x] Users should be able to edit an average rating.
- [x] User should be able to edit Full name.
- [x] User should be able to edit their bio.
- [x] It should be possible to see the catalog site of all items for sale.
- [x] It should be possible to search on a item based on it's name.
- [x] It should be possible to sort the item list after name and price.
- [x] It should be possible to view an item details page when an item is clicked.
- [x] It should be possible to view name, condition, asking price, image, a long description and highest offer of a item.
- [x] It should be possible to view similar items when viewing an item.
- [x] User should be possible to create an item.
- [x] User should be able to select a name, condition, asking price, category, image and a long description.
- [x] User should be able to place an offer on an item.
- [x] User should be able to place multiple offers, until some offer has been accepted.
- [x] User should get a notification when an offer has been placed on their item.
- [x] User should be able to checkout after an offer has been accepter.
- [x] User should be able to fill in his contact information.
- [x] User should be able to fill in his payment information.
- [x] User should be able to reivew the filled out information during the checkout.
- [x] User should be able to confirm checkout purchase.
- [x] It should be possible to navigate throught the header.
- [x] It should be possible to edit profile.

#### Requirements B

- [x] User should be able to edit their email.
- [x] User should be able to edit their username.
- [x] User should be able to view their username.
- [x] User should be able to view their email.
- [x] User should get a notification when their offer has been accepted.
- [x] It should be possible to log out if a user has a registered account.
- [x] It should be possible to rate the seller.
- [x] It should be possible to navigate through the website easily.
- [x] It should be possible to view your own items that are for sale.
- [x] It should be possible to click on the logo in the header to navigate to the homepage.
- [x] It should be possible to insert multiple pictures when creating an item.
- [x] It should be possible to view your own offers.
- [x] It should be possible to delete an item.
- [x] User should land on a 404 page when the url is incorrect.
- [x] User should land on a 403 page when he tries to do something that is forbidden.
- [x] User should be able to view multiple images of an item if the item has multiple images.

#### Requirements C

- [x] It should be possible to view other people's profile.
- [x] It should be possible to edit an item.
- [x] There should be a favicon which displays the logo of the website along with the name.
- [x] There should be a footer with the logo of the website.
- [x] The styling of the website should be clean.
- [x] When inputing a offer, it's only allowed to insert a whole numeric number.
- [x] User should see a confetti when the checkout process is done.
- [x] User should be able to cancel when editing a profile.
- [x] Users should see a red dot when they have notifications.
