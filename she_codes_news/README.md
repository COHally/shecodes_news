# Cathy O Halloran - She Codes News Project

## About This Project

I was tasked with creating a news site that would allow users to read stories and authors to create accounts and write new stories. 

## How To Run This Code
    
1. Clone the repo to your local machine - Navigate to the relevant directory and run the following command:

    - git clone [https://github.com/COHally/shecodes_news.git]

2. Set up Virtual Environment - In your terminal, navigate to the folder containing requirements.txt file:

    - Mac run the following command: source ./venv/bin/activate
    - Windows run the following command: venv/Scripts/activate

3. Install Django:

    - python3 -m pip install -r requirements.txt
    - python3 -m pip freeze (to check if install successful)

4. Migrate Data:

    - cd she_codes_news (to navigate to where manage.py file is contained)
    - python3 manage.py migrate to make migrations

5. Load Data and Run the server:

    - python3 manage.py loaddata news (to load the data for the articles)
    - python3 manage.py runserver (to run the server)

6. Navigate to http://localhost:8000/news in your browser to view the site. 



## Database Schema

![ {{ My ERD }} ]( {{ ./relative_path_to_your_entity_relationship_diagram }} )

## Project Features

- [.] Order stories by date
![ Screenshot of homepage where stories are displayed newest to oldest ](images\Stories - order by date.png )

- [.] Styled "new story" form
![ Form to facilitate the submission of a new story.] (images/New Story Form.png) 

- [.] Story images
![Authors can choose to upload their own image, if not the story will generate a random image.](images\Story Images.png)

- [.] Log-in/log-out
![Login only visible when a user is not logged in, logout only visible when a user is logged in. ] ( images\Login form.png)

- [.] "Account view" page
![ As part of user profile it shows a list of stories the author wrote, username, email and short bio. Please note my url is not working for my profile. To access profile please use the following url: http://localhost:7000/users/3/profile ] (images\Profile.png)

- [.] "Create Account" page
![ Create Account page.  ]( images\Create Account.png)

- [.] View stories by author
![ Search view located in nav will show stories written by name searched. ]  (images\Search Results.png)

- [.] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in
( images\Login.png, images\Logout.png)

- [.] "Create Story" functionality only available when user is logged in
![ In this instance if a user is not logged in and attempt to write a story I have redirected them to the login page. In the instance where they do not have an account I have inserted a link to create account below. ]  ( images\Login form.png)

## Additional Features:
- [ ] Add categories to the stories and allow the user to search for stories bycategory.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Add the ability to “favourite” stories and see a page with your favouritestories.
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Our form for creating stories requires you to add the publication date,update this to automatically save the publication date as the day thestory was first published (maybe you could then add a field to showwhen the story was updated).
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )


