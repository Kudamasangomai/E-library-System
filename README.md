<div align="center">


# E- Library System
  
 An online library management system using Django.

</div>

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/Kudamasangomai/E-library-System.git

```

--> Move into the directory where we have the project files : 
```bash
cd foldername

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :
```bash
envname\scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

### Database was using Postgresql

#

### Functions or modules available:

has an api created using DRF

members can search books by their title, author, subject category

There is a  maximum limit (3) on how many books a member can borrow/issue

there are maximum limit (14) on how many days a member can keep a book.

Members can reserve books that are not currently available then get notification via email upon return of the book

send an email on details of the book a member has borroed

forgot password function is available



