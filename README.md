# Welcome to Project 5 - Fullstack Django 
[![Build Status](https://travis-ci.org/Sonnerz/project05-fullstack-django.svg?branch=master)](https://travis-ci.org/Sonnerz/project05-fullstack-django)


[![Coverage Status](https://coveralls.io/repos/github/Sonnerz/project05-fullstack-django/badge.svg)](https://coveralls.io/github/Sonnerz/project05-fullstack-django)


# The CAM-PAL Issue Tracker

Heroku App: https://fullstack-django-issuetracker.herokuapp.com<br>
GitHub: https://github.com/Sonnerz/project05-fullstack-django<br>


## Guidelines and Guideline fulfilment

1.	**Build a web app that fulfills some actual (or imagined) real-world need. This can be of your choosing and may be domain specific.**<br>
This web app was created to support the end users of a software product called CAM-PAL. The web app allows users to submit bugs for investigation and request features for development.
2.	**Write a README.md file for your project that explains what the project does and the need that it fulfills. It should also describe the functionality of the project, as well as the technologies used. Detail how the project was deployed and tested and if some of the work was based on other code, explain what was kept and how it was changed to fit your need. A project submitted without a README.md file will FAIL.**<br>
Readme supplied
3.	**The project must be a brand-new Django project, composed of multiple apps (an app for each reusable component in your project).**<br>
This is a new Django project composed of seven apps; accounts, blog, cart, checkout, issues, pages & search
4.	**The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. e.g., a user would have to register to persist their shopping cart between sessions (otherwise it would be lost).**<br>
There is an authentication system allowing users to register and log in. It is needed to persist users shopping cart, allow users view their orders and track if the user should have access to the Blog app. <br>
5.	**At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout, subscription-based payments or single payments, etc.**<br>
Users can pay for Feature development and they must do this by purchasing development hours. The purchase of hours is tracked using a cart app and checkout app. Purchases are processed using Stripe.
6.	**Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).**<br>
Users are able to create bugs and edit their own bugs. Users are able to create features and edit their own features. All users can create comments about bugs, and some users can comment on blog posts. Admins can update reported comments and edit all bugs and features.<br>
7.	**The project will need to connect to a database (e.g., SQLite or Postgres) using Django’s ORM**<br>
The project connected to a SQLite database during development and a Postgres database when hosted on Heroku.<br>
8.	**The UI should be responsive, use either media queries or a responsive framework such as Bootstrap to make sure that the site looks well on all commonly-used devices.**<br>
Bootstrap4 and custom css/media queries are used throughout. The site has been tested to prove responsiveness on all commonly-used devices. <br>
9.	**As well as having a responsive UI, the app should have a great user experience.**<br>
I hope the app has a great user experience.
10.	**10.	The frontend should contain some JavaScript logic to enhance the user experience.**<br>
The frontend has AJAX incorporated, to enhance the user experience completing forms.
11.	**Whenever relevant, the backend should integrate with third-party Python/Django packages, such as Django Rest Framework, etc. Strive to choose the best tool for each purpose and avoid reinventing the wheel, unless your version of the wheel is shinier (and if so, consider also releasing your wheel as a standalone open source project).**<br>
Third-Party packages used: 
django-forms-bootstrap, Pillow, dj-database-url, psycopg2, gunicorn, stripe, coverage, codecov, django-filter, django-simple-poll, django-storages, boto3
12.	**Make sure to test your project extensively. In particular, make sure that no unhandled exceptions are visible to the users, under any circumstances. Use automated Django tests wherever possible. For your JavaScript code, consider using Jasmine tests.**<br>
Browser testing using Chrome dev tools was used continuously throughout development. Unit testing  is implemented into each app. As of the deployment date, coverage is at 76%.
CSS and JS was validated using standard online tools. See [Testing](#testing) section.
13.	**Use Git & GitHub for version control. Each new piece of functionality should be in a separate commit.**<br>
Git and GitHub used throughout development with each major update committed.
14.	**Deploy the final version of your code to a hosting platform such as Heroku.**<br>
The final version is deployed to Heroku using AWS to host static and media files.


<hr>
<a id="top"></a>

# Table of Contents

*   [PREFACE](#preface)
*   [Testing Accounts](#acc)
*   [Strategy Plane](#strategy)
    *   [Define roles and responsibilities](#randr)
    *   [Project Charter](#charter)
    *   [Website development Roadmap](#roadmap)
    *   [Strategy Trade-off](#trade)
    *   [Defensive Design](#def)
*   [Scope Plane](#scope)
    *   [Scenarios/User stories](#scenarios)
    *   [Functional Specifications](#func)
    *   [Content Requirements](#content)
*   [Structure & Skeleton Plane](#sands)
    *   [Information architecture](#architecture)
    *   [Database design](#dbdesign)
        *   Database design
    *   [Wireframes](#wireframes)
        *   Home Page
        *   Registration Page
        *   Login Page
        *   Profile
        *   New Feature
        *   Submit Bug
        *   Bug/Feature details
        *   Search Issues/Blog
*   [Surface Plane](#surface)
    *   [Development Phase](#dev)
        *   [IDE Setup](#ide)
            *   vscode
            *   database
            *   Other installations and setup
        *   [Version Control](#version)
        *   [Development](#devtest)
        *   [Testing](#testing)
        *   [Deployment](#deployment)
        *   [Local Deployment](#localdeployment)
*  [Credit](#external)


<a id="preface"></a>

# PREFACE

I have developed a fictitious phone application which can configure a DSLR camera to the optimum settings for that location or subject.
After purchasing the software, the user installs the app on their iOS or Android phone.
By either Bluetooth or WIFI, the phone can connect to the camera, and configure the camera settings to take the best photograph for that environment.
The app can adjust all the standard camera settings such as, ISO, WB, and Focal Point.

I have created a website where customers who register can submit software bugs or request new features to be developed for a fee.
To complete the customer experience, we also provide a blog area paying customers can access.

When a customer submits an issue, that issue is given a unique reference number. Using this number as a form of identity, the customer can follow the progress of that issue from submission, through to issuing a solution.

For a customer to request a new feature they must commit a minimum of €100 to pay for two hours of work reviewing the new feature request. The Developer then updates the feature with the number of hours required to fully develop, test and deploy the new feature. Users can contribute to the development of the feature by buying hours. When the required number of hours specified by the developer has been funded, the feature is then developed.

<a id="acc"></a>
**Accounts**<br>
The assessor can sign up for an account and view the site as a regular user, make purchases and add content.<br>
Alternatively, the assessor can log in using a pre-created account.
This account is a member of a group that can edit/delete other users content and manage reported comments.<br>
Username: assessor<br>
Password: $taticCollect

[Top of page](#top)


# Future updates
1)  ability to assign development to other developers as the site grows
2)  app to log and track development hours against a feature or bug
3)  add rich text editor to Blog

<a id="strategy"></a>

# Strategy Plane
The overall aim of the project is to create a web application that allows users to submit bugs for fixing and pay for additional features. The logic of the app will be written using a variety of technologies but predominantly using the Django framework, jQuery, SQLite and Postgres.  HTML, and CSS will be used to enhance the look and feel of the application, while JavaScript will be used to enhance the user experience.


<a id="randr"></a>

## Define roles and responsibilities
For the purposes of this project, Sonya Cooley has full authority, primary responsibility, and full accountability for all aspects of the project. 
Sonya has a Mentor available to her throughout the development of the application.


[Top of page](#top)
<a id="charter"></a>

## Project Charter 
||Objectives |
|:---|:---|
|**Purpose:** What purpose does the website serve?|The web application is a support site for a software product called CAM-PAL. The web application allows users to submit bugs for fixing and pay for additional features to be developed|
|**Goals:** What outcomes does it need to achieve?|<ul><li>allow users to submit bugs</li><li>allow users to comment about bugs </li><li>allow users to track bugs</li><li>allow users to request new features </li><li>allow users to pay for new features to be developed</li><li>allow users to track feature development</li><li>give paying users access to a Blog</li></ul>
|**Target audience:** Whom must the product appeal to and work for?|<ul><li>Professional photographers</li><li>Amateur photographers</li></ul>|
|**Success indicators:** How will you know you have achieved project goals?|<ul><li>An Increase in the number of people paying for features.</li><li>User interaction via comments and blog posts</li></ul>||
|**Strategies:** What approaches will help to realise the goals?|<ul><li>We will take a mobile first approach to Content</li><li>Provide useful application for submitting bugs</li><li>Aim to keep the site simple and not over complicated</li><li>Present content in a clear and user-friendly way</li></ul>
|**Tactics:** What activities might help to realise the strategies?|<ul><li>Provide useful and relevant content to users</li><li>Provide a user experience that is accessible and enjoyable for all visitors</li><ul><li>Keep site content updated</li><li>following conventions for design and interaction</li><li>providing clear and consistent navigation</li><li>testing usability with a wide range of clients and industry standard tools</li></ul></ul>

[Top of page](#top)
<a id="roadmap"></a>

### Website development Roadmap
The UXD will be driven by the API data and user needs.
|**Define**|Requirements gathering, SEO, Research Competitors,  Content Strategy – Personas, Interesting Content.|
|:---|:---|
|**Design**|Information architecture, Functional & technical requirements, Navigation design, Wireframes, UX/UI, Pages, Branding, style guides, mock-ups.|
|**Develop**|Look & feel, Design and Development, Build, Version control, Testing, Deploy, Read Me|

[Top of page](#top) 

<a id="trade"></a>

### Strategy Trade-off
|Opportunity/Problem|Importance|Viability/Feasibility|
|:---|:---|:---|
|Interesting and fun GUI|5|5|
|Usable GUI|5|5|
|Content|5|4|
|Clever use of technology|4|3|


[Top of page](#top)
<a id="def"></a>

## Defensive Design
Defensive design for our Issue Tracker application will focus on the most common points of failure: user input areas, feedback and server problems.
*   I will employ form validation to check for user mistakes before they frustrate the user
*   I will protect users from server errors and broken links with informative messages
*   My Defensive design will assist the user before mistakes happen.

If users are unsuccessful with any input field, they will be informed by on screen messages that will give clear instructions on how to resolve the issue.
The ‘Registration’ form will ask users to enter a username to appear on the application. They will be informed if that username has already been taken and asked to enter a different username. The form will have validation and offer clear instructions to users on how to proceed.

Every form will have required input fields. Users will be informed via tooltips if they have failed to complete a required field.

Users who attempt to access pages that do not exist will be shown a custom 404 page.
Unregistered Users who attempt to gain access to pages other than the index page will be redirected to the login in page

Registered Users who have not contributed towards feature development and attempt to gain access to the Blog will be redirected to the internal home page - accounts/acc_index/

Environmental variables have been used to protect access details to the database, AWS access and Stripe processing.



[Top of page](#top)
<a id="scope"></a>

# Scope Plane
The project scope is based on our defined Strategy.
Scoping will;
*   fully define the web application requirements 
*   determine the key functionalities
*   determine what features are to be included in this and possible future application releases

The Issue Tracker application will target professional and amateur photographers. A combination of images, and HTML5 will be used to make the interface useful and interesting. Semantic HTML will be used throughout and the site will be responsive to a broad range of devices. 
 
Registered users will be able to add bugs, track their progress and make comments.
Registered users can request new features by paying for the review and development of that feature. A minimum amount will be required to make that request and have it reviewed and a  minimum total amount will be required to develop the feature.

Site content will be stored in SQLite during development and a Postgres database in production. 
Python, Django framework, JavaScript and SQLite and Postgres will be the primary technologies used to implement the web application functionality.




[Top of page](#top)

<a id="scenarios"></a>

## Scenarios/User stories

### Professional photographer:
A professional photographer would have invested in the auto settings app to add it as another tool in their photography kit. They would be keen to submit any issues they had found while using the app as the tool contributes to their livelihood. They would also be interested in expanding the app possibilities by proposing new features which would help in resolving issues that might regularly occur during their commissions.

### Amateur photographer:
An amateur photographer may invest in the auto settings app to help improve their technique or help teach them how to get correct camera settings. 
An amateur will probably only submit bugs for fixing and not invest in any new features. They may not have enough motivation to request new features.


[Top of page](#top)

<a id="func"></a>

## Functional Specifications

The application will provide all registered users with the ability to add bugs and request new features.

Registered users will be able to;
*   add a bug
*   comment on their bug or others users’ bugs
*   track the bug while under review/fix
*   request new features for review by submitting a payment
*   pay for new features to be developed by submitting a payment
*   track the development of the new feature when the development has been fully funded 
*   search for previously submitted bugs by text or reference number
*   search for previously submitted features by text or reference number

Registered users who have requested features will;
*   have access to the Blog
*   be able to add a blog post
*   be able to comment on blog posts
*   search the blog app

The issue tracking application will be optimised for latest version of Chrome, Firefox, Internet Explorer, Safari and Opera and optimised for mobile usage. HTML and CSS will be written using the Mobile-First approach. The mobile-first approach is designing for the smallest screen and working your way up to desktop.

<a id="funcflow"></a>

### Functional Flow

![Functional flow](/readme/ffuncflow.png)


[Top of page](#top)
<a id="content"></a>

##    Content Requirements
The Issue Tracking application will follow a standard format, with a HTML5 structure based on Bootstrap 4. 
The application will have a fixed to top navbar always available to users.

**PAGE :: Home page (/)**

The home page will present users with a welcoming information and the option to log in or register.

**PAGE :: Registration**

The registration form will ask users for; 
*	Email address
*	Username
*	Password
*	Password confirmation


**PAGE :: Log in**

The login form will ask users for; 
*   their previously registered username
*   a password


**PAGE :: Issues home page  (/acc_index)**

The page will list the five most recent submitted issues and requested features.
The page also lists any bugs or features the user has submitted/requested.


**PAGE :: View all bugs  (/issues/)**

The page will display a paginated list of all submitted issues.
Users can filter by the status of the bug.


**PAGE :: Submit a bug  (/issues/new/)**

The page will allow a user to submit a bug. 
Menu options:
*   Title
*   Details
*   Image
*   Tag
*   Published date (readonly)

**PAGE :: View all features (issues/all_features/)**

The page displays a paginated list of all requested features.
Users can filter by the status of the feature.


**PAGE :: Request a feature  (/issues/newfeature/>**

The page will allow a user to request a new feature for review.
A minimum of 2 hours must be paid before a new feature request is reviewed.
Menu options:
*   Title
*   Details
*   Tag
*   Published date (readonly)
*   Cost per hour (readonly)
*   Hours set to 2 (readonly)


**PAGE :: Bug detail page (/issues/<bug-id>/)**

The page will list all a bugs details.
It also displays a paginated list of comments added by users about this bug. 
Menu options:
*   Edit bug if the user authored the bug
*   Comment on bug – everyone
*   Vote up bug if user did not author the bug
*   Admin Edit if the user is an admin


**PAGE ::  Feature detail page (/issues/<feature-id>)**

The page will list all feature details. 
Menu options:
*   Edit feature if the user authored the feature
*   If ‘Target not Reached’ status, a Donate button
*   Admin Edit if the user is an admin


**PAGE ::  Profile page (/accounts/profile/)**

The page will list all users’ orders. 

**PAGE ::  Search (/search/?q=)**

The search results page displays a paginated list of search results.
The search will allow users to; 
*   search by bug or feature reference
*   search words in the bug or feature title

**PAGE ::  Cart (/cart/)**

The cart page;
*   displays the feature details
*   how many hours the user is buying
*   allows the user to adjust these hours

**PAGE ::  Checkout (/checkout/)**

The checkout page;
*   displays an order summary and final total
*   displays a form for gathering user information and
*   credit card information


**PAGE ::  Blog (/blog/)**

Accessible by users who have made a contribution towards feature development.
*   displays a paginated list of blog posts

**PAGE ::  Blog (/blog/new/)**

The page will allow a user to add a blog post. 
*   Title
*   Content
*   Image
*   Tag
*   Published date (readonly)

**PAGE ::  Blog (/blog/<blog_id>/)**

The page displays a blog post contents. 
*   Title
*   Content
*   Image
*   Tag
*   Published date (readonly)

Menu options:
*   Edit post if the user authored the post
*   Delete the post if the user authored the post
*   Comment on post – everyone

**Navigation**

The navbar will be available to users at the top of the application on every page.<br>
Unregistered users will see links to Login, Register, About us, Examples, & About this site.<br>
Registered users will see links to Logout, Cart, & Profile.<br>
Registered users who have contributed towards feature development will see links to Logout, Cart, Profile & Blog.



[Top of page](#top)

<a id="sands"></a>

#  Structure & Skeleton Plane

Our goal for the Structure plane is to organise the information architecture and interactions for the application. We will keep a consistent, predictable, and learnable interface that users should be familiar with if they regularly use the internet. We will use industry standard technologies to implement expected behaviours when using the application, e.g. tooltips, navigation, including accessibility, etc.
Users will find navigation and user information at the top of the application. 
The input fields will follow user expectations where feedback is provided if user interactions are unexpected, correct or incorrect.



<a id="architecture"></a>
## Information architecture
The application directories and files will be organised in the following way;

<ul><li>Site Root</li><ul><li>App: accounts</li><li>App: blog</li><li>App: cart</li><li>App: checkout</li><li>App: htmlcov</li><li>App: issues</li><li>Project: issuetracker</li><li>media</li><li>App: pages</li><li>App: search</li><li>static</li><li>templates</li><li>.gitignore</li><li>.travis.yml</li><li>custom_storages.py</li><li>manage.py</li><li>Procfile</li><li>requirements.txt</li><li>ReadMe.md</li></ul></ul>



[Top of page](#top)

<a id="dbdesign"></a>

##  Database design

![Database design scheme](/readme/issues_db.png)

Database is SQLite in development and Postgres in production.
The tables shown are the tables I have added and do not include the default Django tables (except the auth_user)


[Top of page](#top)
<a id="wireframes"></a>
##  Wireframes

## Home Page (‘/’ index.html) <a id="homewf"></a>
![home page](/readme/home.png)

## Registration Page (‘/register/) <a id="signwf"></a>
![registration page](/readme/sign_up.png)

## Login (‘/login/) <a id="lloginwf"></a>
![login page](/readme/login.png)

## Profile  (‘/profile/) <a id="mywf"></a>
![profile page](/readme/profile.png)

## New Feature (/issues/newfeature/) <a id="recipewf"></a>
![New feature](/readme/add_feature.png)

## Submit Bug (/issues/new/) <a id="addwf"></a>
![Submit Bug](/readme/add_bug.png)

## Bug/Feature Detail (/issues/<bug_id>)(/issues/<feature_id>/features) <a id="addwf"></a>
![Bug/Feature detail](/readme/bug_details.png)

## Search results (/search/?q=<searchparam>) <a id="wfsearch"></a>
![Search](/readme/search.png)


[Top of page](#top)
<a id="surface"></a>
#  Surface Plane

<a id="dev"></a>
## Development Phase

<a id="ide"></a>

### IDE - SETUP - VSCODE

1.	After opening vscode I created a workspace
2.	And created a Virtual Environment: py -3.6 -m venv venv
3.	Install Django-1.11 in the virtual env:  pip3 install Django 1.11
4.  GitHub has a security issue with 1.11: pip uninstall django && pip install django==1.11.15
5.	Debug - Open Configurations-Python to configure launch.json
```
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "console": "integratedTerminal",
            "args": [
                "runserver",
                "--noreload",
                "--nothreading"
            ],
            "django": true
        }
```
6.	Create Django Project: django-admin startproject issuetracker  .
7.	Migrate Databases: python manage.py migrate
8.	Create superuser: python manage.py createsuperuser
9.	Create regular user: Using admin site
10.	settings.py: ALLOWED_HOSTS = ['127.0.0.1']
11.	TEST to ensure Django is successfully installed and running: Debug – run
12.	requirements.txt: pip3 freeze --local > requirements.txt
13.	Procfile: echo web: gunicorn issuetracker.wsgi:application > Procfile
14.	Python Linter: pip install -U autopep8
15.	Create env.py to store environmental variables
16.	Git:  git init
-   echo '*.sqlite3' >> .gitignore
```
-   *.pyc
-   .vscode
-   __pycache__
-   venv
-   *.code-workspace
-   env.py
```
-   git add .
-   git commit -m “initial commit”
-   $ git remote add origin https://github.com/Sonnerz/project05-fullstack-django.git 
-   $ git push -u origin master
17.	Travis CI:
-   Sync Travis account with GitHub account
-   Connect GitHub repository project05-fullstack-django
-   Get Markdown Status image and copy into README.md
-   Create .travis.yml file
```
language : python
before_install:
- chmod +x manage.py
python:
- "3.6"
install: "pip install -r requirements.txt"
script:
- SECRET_KEY="something" ./manage.py test 
```
18. Push to GitHub and ensured that Travis CI status is build:passing


### IDE - SETUP - DATABASE

1.	I installed DB Browser for SQLite fpr local development
2.  pgAdmin 4 for viewing the LIVE database


### IDE - SETUP - Other installations and setup

*   **Bootstrap forms fo styling forms**:	pip3 install django-forms-bootstrap
*   **Pillow to enable users upload images***:	pip3 install Pillow
*   **database-url for Postres DB**:	pip3 install dj-database-url
*   **psycopg2 for Heroku**:	pip3 install psycopg2
*   **Stripe support**:	pip3 install stripe
*   **coverage for unittesting**:	pip3 install coverage
*   **coveralls**:	pip install coveralls
*   **django-filter for filtering search results**:	pip install django-filter
*   **simple-poll for a user poll**:	pip install django-simple-poll
*   **django-storages for AWS**:	pip3 install django-storages
*   **boto3 for AWS**:	pip3 install boto3
*   **gunicorn for Heroku**:	pip3 install gunicorn

[Top of page](#top)

<a id="version"></a>
### Version Control

Git was used to manage the source code for this project. Git is a version control system for tracking changes in project files.
Project files were committed to Git after each major functional addition, update or implementation of testing results.
Following the initial commit to Git, each major update was followed by a Git add and commit. 
**A full Git log is available on the GitHub project repository**.


[Top of page](#top)

<a id="devtest"></a>

### Development

##  HTML
HTML5 is used throughout and the following themes were implemented.
https://bootswatch.com/superhero/	: is used for the issues site<br>
https://bootswatch.com/spacelab/	: is used for the blog app<br>


##  CSS
Custom css and bootstrap overrides can be found at static/css/styles.css
The css has been validated.


##  Python
The web app follows the standard Django pattern; forms, models and views.
The following apps are based on apps created during course lessons: accounts, cart, checkout and search. I have used them as a starting point and customised them for my project.


##  jQuery
jQuery is implemented on the registration form and password reset form. It has been validated.
*   The jquery on the registration form checks the database for the username and ensures that the username entered is unique.
*   The jquery on the password reset form checks the database for the email and ensures that the email exists in the database.
*   jQuery is used to set some form fields to readonly.
*   jQuery is used to show/hide the donate form on the feature details page.
*   jQuery is used to add a css class to the link to highlight it as being active.
*   jQuery styles the button for the status filter.
*   jQuery applies Smooth scrolling to the home page


[Top of page](#top)

<a id="testing"></a>

## Testing

The app was tested on an ongoing basis. Chrome and Chrome Developer Tools were the primary browser and tool used for testing. However, the site was also tested using Firefox and Internet Explorer.
*   CSS passed validation using the CSS Validation Service provided by The World Wide Web Consortium (W3C): https://jigsaw.w3.org/css-validator/
*   Pep8 was used to apply a standard coding convention to the Python code
*   PyLint was also installed and used
*   All the functions in custom_scripts.js were validated on http://jshint.com/
This site is a tool that helps to detect errors and potential problems in JavaScript code.

#### During development:
*   print() was used extensively for viewing returned data and testing. 
*   Console.log() was used viewing the ajax response and testing. 
*   Div’s had vibrant background colours so that the developer was easily able to identify them
*   Each change was viewed in a chrome browser and tested using developer tools at full width resolution and using a variety of device emulators; Galaxy SIII, Galaxy 5, Laptop touch screen, iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 Plus, iPhone X, iPad.
*   The site was pushed to Heroku and tested on mobile devices.

#### Development/Defensive Design Testing
Testing was carried out continuously while developing the app. New functionality was tested in the browser until it was working as expected.

As per the Defensive Design Strategy described in the Strategy Plan, all form inputs are checked for empty values. Users are messaged if they click a submit button without providing text.

Debug mode was set to False to test 500 and 404 errors.

![Username taken](/readme/un.png)


<a id="ongoing"></a>

### Ongoing Testing

|Page/functionality|Chrome|Firefox|IE|Chrome Android-Remote Debugging|
|:---|:---:|:---:|:---:|:---:|
|All html pages|General formatting issues|General formatting issues|General formatting issues|General formatting issues|
|Responsive Design|Styling issues|Styling issues|Styling issues|Styling issues|
|Feedback messages appear|Passed|Passed|Passed|Passed|
|Admin Buttons hidden|Regularly tested under different access levels|Regularly tested under different access levels|Regularly tested under different access levels|Regularly tested under different access levels|

<br><br>

|Device/Test|Galaxy SIII|Galaxy 5|Laptop touch screen|iPhone 5/SE|iPhone 6/7/8|iPhone 6/7/8 Plus|iPhone X|iPad|
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Pages with buttons|Buttons too wide|Buttons too wide|N/A|Buttons too wide|Buttons too wide|Buttons too wide|Buttons too wide|N/A
|Styling|Ongoing development|Ongoing development|Ongoing development|Ongoing development|Ongoing development|Ongoing development|Ongoing development|Ongoing development|
|Left Nav buttons|not wrapping|not wrapping|N/A|not wrapping|not wrapping|not wrapping|not wrapping|not wrapping


### User Testing

**Issues and Resolution**

1) After editing a bug the screen redirects to all bugs view<br>
    -  This was changed to redirect back to the bug details screen
2) yellow debug screen for a 404
    -  I set debug to False on settings.py
3) View feature details button overflows on a mobile
    -  I shortened the button text
4) Burger menu off screen on mobile
    -  This was related to the issue 3. The button was pushing the burger off screen
5) Don't know what status user filtered by
    -  Change the view code to get the request status and passed it back to the page as a variable. This gives user feedback.


### Unit Testing

Each app has its own python test file for app, forms and views.
Currently Coverage shows 76% complete.

[Top of page](#top)

<a id="deployment"></a>

## Deployment

- pip3 install dj-database-url (ensure this is installed)
- pip3 install psycopg2 (ensure this is installed)
- **GitHub** is used to host the code and Heroku was used to host the app.
- **Travis** account synced with GitHub repo : project05-fullstack-django.
- **Heroku**: created a postgres DB
- **Heroku**: Add env vars; SECRET_KEY, STRIPE_PUBLISHABLE, STRIPE_SECRET, DISABLE_COLLECTSTATIC
- **env.py**: add postgres url as env var; os.environ.setdefault("DATABASE_URL", "postgres...)
- **settings.py**:  allowed hosts[] - add fullstack-django-issuetracker.herokuapp.com
- **settings.py**: Database config;
```
if "DATABASE_URL" in os.environ:
    DATABASES = {'default': dj_database_url.parse(
        os.environ.get('DATABASE_URL'))}
else:
    print("LIVE Postgres database not found, using development SQLite DB instead.")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
- $ python manage.py makemigrations 
- $ python manage.py migrate (update postgres db with tables)
- $ python manage.py createsuperuser
- Created an AWS account:
    -   S3 Service: Created a Bucket with a Public read access
    -   IAM service: created a Group
    -   IAM service: create a Policy based on AmazonS3FullAccess
    -   IAM service: attached policy to group
    -   IAM service: create user, give user the group perms
    -   Download CSV keys

- pip3 install django-storages
- pip3 install boto3
- pip3 install gunicorn
- pip3 freeze > requirements.txt

- **Env.py**: set up env with AWS details; 
- **Heroku**: add AWS env vars to the app: AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID
- **Settings.py**: add all required vars for App connecting with AWS (see settings.py)


**GitHub**

1   A new repository was created in GitHub called: `project05-fullstack-django`
After a final Git Add and Git commit

1.  `git add.`
2.  `$git commit -m "Final commit"`
The pages were pushed to the new GitHub repository
5.  `$ git remote add origin https://github.com/Sonnerz/project05-fullstack-django`
6.  `$ git push -u origin master`
7.  `Enter: _username_`
8.  `Enter: _password_`

Heroku is used to host the code and publish the app publicly.

I logged into Heroku and created a new app called **fullstack-django-issuetracker**<br>
I chose the European hosting region<br>
A git repo was created: https://git.heroku.com/fullstack-django-issuetracker.git<br>
A heroku app url was provided: https://fullstack-django-issuetracker.herokuapp.com<br>
I synced the Heroku app with the GitHub repo


**Issues and Resolution**

There were many trial and errors. Mainly the coveralls failed.
I found it difficult to get codecov and coveralls to work on Travis.
I tried codecov and then coveralls.


[Top of page](#top)

<a id="localdeployment"></a>

## Local Deployment

To deploy this project locally;
1) Download the project from GitHub
2) Create a local virtual environment and install the packages listed in the requirements.txt
3) This should create a local SQLite database with the Django installation
4) Create a superuser account
5) Run makemigrations
6) Run migrate
7) Create a local env.py file in the root of your site
8) Create a local env var for; SECRET_KEY, STRIPE_PUBLISHABLE, STRIPE_SECRET, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, EMAIL_ADDRESS, EMAIL_PASSWORD
9) Your project should run on 127.0.0.1/8000. This is the Django default local url.
10) Note, this database will be empty of content.

<a id="external"></a>

# Credit

##  Content/ Acknowledgements

The following sites were used as resources to get sample css and debugging css.

|Site|URL|Resource
|:---|:---|:---|
|Stack Overflow| http://stackoverflow.com | Code snippets/idea throughout the project
|w3schools Python| https://www.w3schools.com/python |HTML, CSS, Python
|Startbootstrap| https://startbootstrap.com |Agency template
|Slack|Code Institute slack|Slack members user tested my application
|Bootswatch|https://bootswatch.com/superhero/https://cdnjs.cloudflare.com/ajax/libs/bootswatch/4.1.3/superhero/bootstrap.min.css|Superhero theme for issues app
|Bootswatch|https://cdnjs.cloudflare.com/ajax/libs/bootswatch/4.1.3/spacelab/bootstrap.min.css|Spacelab theme for Blog app
|Youtube - Mike Hibbert|https://www.youtube.com/watch?v=qLRxkStiaUg|How to extend the Django User object
|SIMPLEISBETTERTHANCOMPLEX By Vitor Freitas|https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html#testing-the-sign-up-view|Unit-testing
|Agiliq|https://www.agiliq.com/blog/2013/04/common-testing-scenarios-for-django-app/|Common unit testing scenarios
|SIMPLEISBETTERTHANCOMPLEX By Vitor Freitas|https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html|Django Pagination


##  Media

|Media|Scource||
|:---|:---|:--|
|Images|Canon owns the camera image. Samsung owns the mobile image
|Images|Fireworks and Joshua tree owned by developer
|Images|Other images used are credited


[Top of page](#top)



