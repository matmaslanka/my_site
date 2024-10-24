# My site
A blog application based on Django where the user can add posts from the admin panel. Logged-out users can add comments and save posts to their 'read later' page within the session.

## Installation

1. Clone the repository:
   `git clone https://github.com/matmaslanka/my_site.git`
2. Set up a virtual environment:
   python3 -m venv env <br/>
   source env/bin/activate  # On Windows: env\Scripts\activate
3. Install the dependencies from requirements.txt:
   `pip install -r requirements.txt`
4.  Open a terminal and navigate to the project directory in bash: 
   `cd .\my_site`
5. Add your own secret key to `my_site\settings.py` on line 24.
   Example: "0ne2fxv8vpeisxbd1xtq2kx-vnlv_7bnf%8nwc+jj(bpoe3_@v"
   (Note: The secret key is hidden for security reasons.)
6. Set up the database and run migrations (the application will crash without this step):
   `python manage.py migrate`

## Running the project
1. Run the Django development server:
   `python manage.py runserver`
2. Access the project in your browser at: http://127.0.0.1:8000/.

## Usage

When the user runs the application, they will see a homepage. The navigation bar contains three tabs: "Mati's Blog," which takes the user back to the starting page; "Stored Posts," where the user can store posts to read later; and "All Posts," which redirects to a page displaying all posts.

On the homepage, the three latest posts are displayed.

By clicking on a post from the Homepage, Stored Posts, or All Posts, the user can read the post and its comments. They can also add a comment by filling out the comment form.

### Admin Access
(Optional) To access the Django admin interface, create a superuser account:
   `python manage.py createsuperuser`
