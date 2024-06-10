# :purple_circle: *BalconyGrown* :purple_circle:

 🌱 The deployed page can be found [here]() 🌱


## Table of Contents

- [Objective](#objective)
- [Business Goals](#business-goals)
- [Marketing](#marketing)
- [User Stories](#user-stories)
- [Key Features](#key-features)
- [Design](#design)
- [Testing](#testing)
  - [Official Validators](#official-validators)
  - [Bugs](#bugs)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Project Status](#project-status)
- [Acknowledgements](#acknowledgements)

## Objective

- Hands-on learning by building an FullStack E-Commerce Platform
- Learning usage of Agile Methodology using Gibhub Projects, working with their [Kanban board](https://github.com/users/zabokaa/projects/3/views/2) + labels plus milestones for [Issues](https://github.com/zabokaa/vina/issues). It will be very valuable when working in a team in the future.

## User Stories

### As a Guest-user [...]

- I want to easily navigate the site.
- I want to be able to create my own profile.
- I want to be able to add products to my shopping bag.
- I want to know when a product is out of stock or has less than 5 products.
- I want to have a smooth check out process.
- I want to be informed about all changes I make to my order. 

### As a Logged-in-user [...]

- I want to see my order history
- I want to save my delivery data for easier next shopping experience.
- For data security I do not want my payment data been saved in my account. 

### As a Super-user = Admin [...]
- I want to add, edit, and delete products
- I want to see the current in_stock of each product
- I want that the stock is up to date, after each successfull checkout.
- I want to update the in_stock after receving a new delivery.

## Key Features

## Models

Entity Relationship Diagram:

  ![ERD](./media/readme/ERD_balconyGrown.pdf)


## Testing


### Official Validators

- W3C HTML Validator: No errors
- W3C CSS Validator:  No errors
- CI Python Linter:  No errors
- Lighthouse Chrome DevTools are oki. 


### Bugs

#### Unsolved
- Problems with deploying the project on Heroku. 

## Technologies

Python | HTML | CSS | JavaScript | Django | Bootstrap5 | Whitenoise | Gunicorn | Crispy | Neon Postgres DB | Cloudinary | Heroku

## Project Status

Project is: in process.
There are still a few thing to do: e.g I want to add a voucher model.
Content in the About section is missing.

## Deployment

  From How to Start a Django Project till Access to your Deployed Site:

1. **Start a Django Project:**
   Open your terminal (I am working wiht VS Code) and navigate to the directory where you want to create your project. Run the command `django-admin startproject your_project_name`.

2. **Create a New Django App:**
   Navigate into your new project directory with `cd your_project_name` and run the command `python manage.py startapp your_app_name`.

3. **Create a Model:**
   In your new app directory, open the `models.py` file and define your model classes.

4. **Create a View:**
   In the same app directory, open the `views.py` file and define your view functions or classes.

5. **Update URLs:**
   Update the `urls.py` files in your project and app directories to route to your new views.

6. **Run Migrations:**
   Run `python manage.py makemigrations` and `python manage.py migrate` to create and apply migrations for your new models.

7. **Test Your App Locally:**
   Run `python manage.py runserver` to start the development server and access your app in your web browser.

8. **Login to Heroku:**
   Run `heroku login` and enter your Heroku credentials.

9. **Create a New Heroku App:**
   Navigate to Heroku and click on "New" > "Create new app". Enter the app name (e.g., "goodfood"), and click "Create app".

10. **Update Settings:**
    Update your `settings.py` file to be compatible with Heroku. This includes setting `DEBUG` to `False` (always before deploying with Heroku!), adding your Heroku app URL to `ALLOWED_HOSTS`, and configuring your database to use Neon Postgres.

11. **Back to Heroku Configure Environment Variables:**
   Navigate to "Settings" > "Config Vars" and click "Reveal Config Vars". Add a new variables with the keys for `SECRET_KEY`, for connecting to Database `DATABASE_URL`, and for storaging media files in a cloud aswell `CLOUDINARY_URL`

12. **Connect with GitHub:**
   Navigate to the "Deploy" section, connect with GitHub, and choose your repository name.

13. **Choose Deployment Method:**
   Decide if you want to deploy manually or enable automatic deployment after every commit to GitHub.

14. **Access Your Deployed Site:**
   Once done, your application will be live. Yippie!

15. **Access Your Deployed Site:**
    Once the build is successful, you can access your deployed site using the URL provided by Heroku.

16. **Clone and Install Dependencies:**
   If you want to clone this repository, you can easily install all necessary versions and libraries using `pip install -r requirements.txt`.

## Acknowledgements

- This project is based on full-stack course @ Code Institute, especially the Walk-through-project Boutique-Ado
- All images from Pexels 
