<h1 align="center">AirBnB - Project at Holberton School</h1>
<br>

Welcome to the first project of AirBnB clone, this project consists of developing a console of AirBnb from scratch, that allows users to search, create and manage models.

![AirBnB](https://github.com/JeremiasInCode/holbertonschool-AirBnB_clone/assets/80486569/dce407ed-aafa-4741-8019-bdb02936665b)

<br>

# Requirements

To use this command-line interpreter, you will need:

## Python 3.6 or later.
- The interpreter is built using Python programming language. Therefore, it is essential to have Python 3.6 or a later version installed on your system. You can download and install Python from the official Python website (https://www.python.org) or use a package manager specific to your operating system.
  
## Basic console knowledge.
- Familiarity with basic console operations is necessary to navigate and interact with the command-line interpreter. You should be comfortable with executing commands, navigating directories, and managing files using the command prompt or terminal of your operating system.

<br>

<h2> Installation: </h2>
<h3> To have access to the console use the following command: </h3>

```
git clone https://github.com/JeremiasInCode/holbertonschool-AirBnB_clone.git
```

<h2> Start the console: </h2>
<h3>If you want to execute the console use:</h3>

```
python3 console.py
```
or

```
./console.py
```

## Commands

| Método    | Descripción                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------|
| create    | Creates a new instance of BaseModel, saves it in the JSON file and displays the id.                            |
| show      | Prints the string representation of an instance based on the class name and id.                                 |
| destroy   | Deletes an instance based on the class name and id (saves the change in the JSON file).                         |
| all       | Prints the string representation of all instances, whether based on the class name or not.                      |
| update    | Updates an instance based on the class name and id by adding or updating an attribute (saves the change in the JSON file). |

<br>

## Classes
| Class name | Attributes                                                                                                 |
|------------|-----------------------------------------------------------------------------------------------------------|
| BaseModel  | created_at, updated_at, id                                                                                |
| User       | first_name, last_name, email, password                                                                    |
| State      | name, state_id                                                                                            |
| City       | name                                                                                                      |
| Amenity    | name                                                                                                      |
| Place      | name, description, number_rooms, city_id, user_id, price_by_night, max_guest, number_bathrooms, longitude, latitude, amenity_ids |
| Review     | place_id, user_id, text                                                                                    |

<br>

## Authors

* **Jeremias Erba** - *Holberton Student* - [Jeremias Erba](https://github.com/JeremiasInCode/) - *Software development.*
* **Mateo Olivera** - *Holberton Student* - [Mateo Olivera](https://github.com/MateoOlv) - *Software Developer.*
