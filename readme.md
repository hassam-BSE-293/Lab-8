# Fitness Pro Gym - Gym Management System

A web-based Gym Management System built with Flask, HTML, and CSS. This website provides information about the gym, its facilities, team, and membership plans.

## Features

- **Home Page**: Welcome message and key highlights of the gym (Modern Equipment, Certified Trainers, Flexible Timings)
- **About Us Page**: Information about the gym's mission, team members, and available facilities
- **Membership Page**: Display of different membership plans with pricing and features

## Project Structure

```
GYM_WEBSITE/
│
├── app.py                 # Main Flask application file
├── README.md             # Project documentation
│
├── templates/            # HTML template files
│   ├── base.html        # Base template with header and footer
│   ├── Home.html        # Home page template
│   ├── About.html       # About Us page template
│   └── membership.html  # Membership page template
│
└── static/              # Static files (CSS, images, etc.)
    └── style.css        # Main stylesheet
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3
- **Template Engine**: Jinja2 (Flask's built-in templating)

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/hassam-BSE-293/gym-website.git
   cd gym-website
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Flask**
   ```bash
   pip install flask
   ```

## Running the Application

1. Make sure you're in the project directory and your virtual environment is activated

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

4. The website should now be running locally on your machine!

## Usage

- Navigate through the website using the navigation menu
- **Home**: View gym highlights and welcome message
- **About Us**: Learn about the team and facilities
- **Membership**: Browse available membership plans

## Routes

The application includes the following routes:

- `/` or `/home` - Home page
- `/about` - About Us page
- `/membership` - Membership plans page

## Sample Membership Plans

The membership page displays various plans with different features:
- **Basic Plan**: Access to gym and locker facility
- **Premium Plan**: All basic features + Personal trainer + Nutrition consultation
- *(Plans can be customized in app.py)*

## Future Enhancements

Potential features to add:
- User registration and login system
- Online membership payment integration
- Class schedule and booking system
- Trainer profiles and booking
- Member dashboard
- Contact form

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For any queries or suggestions, please contact:
- **Project Maintainer**: Muhammad Hassam
- **Email**: mhassam2505@gmail.com
- **GitHub**: [@hassam-BSE-293](https://github.com/hassam-BSE-293)

---

**Note**: This is a basic demonstration project created for learning purposes. For production use, additional security measures and features should be implemented.