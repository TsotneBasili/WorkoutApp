WorkoutApp
Welcome to WorkoutApp, a Django-based web application that helps you manage and track your workouts, weight, and fitness goals. This project is organized into four main apps: track, workout_plan, user, and workoutapp. Below, you'll find an overview of each app along with instructions on how to set up and run the project.

Apps
track
The track app is responsible for managing weight entries and fitness goals.

Models:
WeightEntry: Records user-specific weight entries with date and weight details.
FitnessGoal: Allows users to set fitness goals such as weight targets and exercise achievements.

Views:
WeightEntryListView: Displays a list of weight entries, allows creation, retrieval, and updates.


workout_plan
The workout_plan app enables users to create, manage, and track workout plans and exercises.

Models:
Exercise: Describes various exercises with details such as name, description, instructions, and target muscles.
WorkoutPlan: Represents user-specific workout plans, including workout frequency, goals, exercise types, repetitions, sets, session duration, and distance.

Views:
WorkoutPlanView: Provides CRUD operations for workout plans, including the ability to list, create, retrieve, update, and delete.
ExerciseView: Manages exercises, allowing users to list, create, retrieve, update, and delete.


user
The user app handles user authentication and authorization.

Features:
User authentication and authorization.


workoutapp
The workoutapp app serves as the main app, defining settings and URLs for the project.

Features:
Main settings and URLs.


Access the APIs with JWT authentication:
Use JWT tokens for authentication. Refer to the Swagger documentation for details on obtaining and using JWT tokens.

1. **Clone the repository:**
    ```bash
    git clone https://github.com/TsotneBasili/WorkoutApp.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd WorkoutApp
    ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5. **Run migrations:**
    ```bash
    python manage.py migrate
    ```
6. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

Docker Support
If you prefer using Docker, a Dockerfile is provided for your convenience. Build the image and run the container:
in bash:
1. **Building Image:**
```bash
docker build -t workoutapp .
```
2. **Starting Project:**
```bash
docker run -p 8000:8000 workoutapp
```
3. **Accesing the Application:**
```bash
Access the application at http://localhost:8000/
```
