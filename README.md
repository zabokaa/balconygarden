# :purple_circle: *BalconyGrown* :purple_circle:

xxxxxxxxx

 ![mockup]()

 🌱 The deployed page can be found [here]() 🌱

If you do not want to register for testing the functionality of the E-Commerce feel free to use: 

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


## Business Goals

## Marketing

## User Stories

### As a Guest-user [...]

- I want to read recommendations (posts and comments).
- I want to easily navigate the site.
- I want to be able to create my own profile.

### As a Logged-in-user [...]

- I want to add and delete wines to my private library/vinotheque.
- I want to commment on my own or others users' post.
- I want to be able to edit or delete my comments.
- I want to see if I am logged-in or not.
- I want to see the list of all my liked Posts, and being transferred to that one when clicking on it.
- I want to create a new Wine Diary entry, where I can decide by myself if I want to add an image, a memory text, or a foodpairing hint.
- I want to see a list of all my diaries (or "nor entries yet" when there are none) with name of wine, ordered by my rating.
- I want to display the specific diary entry when clicking on the name.
- I want to delete a diary entry.

### As a Super-user = Admin [...]

- I want to to approve or disapprove user's new entries/posts
- I want to approve or dissaprove comments on existing entries.

## Key Features

## Models

The Viña project has 5 models:

- Post model in the blog app is based on the Walkthrough project, and highly customized by me.
- Comment model in the blog app is based on the Walkthrough project.
- Diary model in the vinoteka app completely created by me.
- User model created by Django AllAuth.

Entity Relationship Diagram:

  ![ERD](./assets/ERD_balconyGrown.pdf)

## Design

### Colors

green

### Logo

   ![logo](./static/img/vinalogo.png)

The goal was for the logo to be both classic and hipster-modern, aiming to appeal to a wide range of age groups. Various age target groups should feel equally addressed. Additionally, the logo should not distract from the content. Therefore, it is kept monochromatic, in the secondary color.

## Testing

[HERE](./testing.md) are my steps of manually testing all User Stories. Since this project is relatively small and not too complex, manual testing is more efficient. Furthermore, I can check for UX.

### Official Validators

- W3C HTML Validator [HERE](./assets/imgreadme/htmlchecker.png): No errors
- W3C CSS Validator [HERE](./assets/imgreadme/jigsaw.png.png):  No errors
- CI Python Linter [HERE](./assets/imgreadme/pylinter.png):  Some lines too long error -> formated code -> No errors
- Lighthouse Chrome DevTools [HERE](./assets/img/lighthouse.png)
Have been sucessfully tested for all pages, just displaying 1 example for each validator.

### Bugs

#### Solved

#### Unsolved

## Technologies

Python | HTML | CSS | JavaScript | Django | Bootstrap5 | Whitenoise | Gunicorn | Crispy | Neon Postgres DB | Cloudinary | Heroku

## Project Status

Project is: in process

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

- This project is based on full-stack course @ Code Institute, especially the Walk-through-project "I Think Therefore I Blog"
- Images from Pexels or mine
