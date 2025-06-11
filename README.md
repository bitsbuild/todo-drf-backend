# 📝 ToDo REST API

A simple Django + Django REST Framework API for managing ToDo tasks.

---

## 🛠️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/bitsbuild/todo-drf-backend-for-learning.git
cd todo-drf-backend-for-learning/todo

# 2. Create and activate a virtual environment (recommended)
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
```

Once the server is running, the API will be available at:

```
http://127.0.0.1:8000/todo/
```

---

## 🔗 URL Configuration

### Project-Level (`project/urls.py`)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todorestapi.urls')),
]
```

### App-Level (`todorestapi/urls.py`)
```python
from django.urls import path
from todorestapi.views import (
    add_an_item,
    get_all_to_do_items,
    get_specific_to_do_item,
    remove_an_item,
    update_an_item,
    mark_as_done,
)

urlpatterns = [
    path('api/tasks/', get_all_to_do_items),
    path('api/tasks/find/<uuid:id>/', get_specific_to_do_item),
    path('api/tasks/add/', add_an_item),
    path('api/tasks/update/<uuid:id>/', update_an_item),
    path('api/tasks/delete/<uuid:id>/', remove_an_item),
    path('api/tasks/mark-done/<uuid:id>/', mark_as_done),
]
```

---

## 📚 API Endpoints Documentation

All endpoints are prefixed with:
```
http://127.0.0.1:8000/todo/api/tasks/
```

---

### 🔹 GET `/api/tasks/`
**Description:** Fetch all ToDo tasks.

- **Method:** `GET`
- **Response:** `200 OK`
- **Response Format:**
```json
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "task_name": "Buy groceries",
    "task_description": "Milk, Bread, Eggs",
    "is_completed": false,
    "created_at": "2025-06-11T10:30:00Z"
  },
  ...
]
```

---

### 🔹 GET `/api/tasks/find/<uuid:id>/`
**Description:** Fetch a specific task by its UUID.

- **Method:** `GET`
- **Path Param:** `id` (UUID of the task)
- **Response:** `200 OK`
```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "task_name": "Buy groceries",
  "task_description": "Milk, Bread, Eggs",
  "is_completed": false,
  "created_at": "2025-06-11T10:30:00Z"
}
```

---

### 🔹 POST `/api/tasks/add/`
**Description:** Add a new task.

- **Method:** `POST`
- **Request Body:**
```json
{
  "name": "Finish assignment",
  "desc": "Complete Django project"
}
```
- **Response:** `201 Created`
```json
{
  "Status": "Task Creation Successfully"
}
```

- **Error (e.g., missing fields):**
```json
{
  "Status": "Task Creation Failed"
}
```

---

### 🔹 PUT `/api/tasks/update/<uuid:id>/`
**Description:** Update the name and description of an existing task.

- **Method:** `PUT`
- **Path Param:** `id` (UUID of the task)
- **Request Body:**
```json
{
  "name": "Update title",
  "desc": "Change description text"
}
```
- **Success Response:** `200 OK`
```json
{
  "message": "task update successful"
}
```

- **Failure Response:** `400 Bad Request`
```json
{
  "message": "task update failed"
}
```

---

### 🔹 DELETE `/api/tasks/delete/<uuid:id>/`
**Description:** Delete a task using its UUID.

- **Method:** `DELETE`
- **Path Param:** `id` (UUID of the task)
- **Response:** `200 OK`
```json
{
  "message": "required object delete"
}
```

- **Failure Response:** `400 Bad Request`
```json
{
  "message": "could not delete"
}
```

---

### 🔹 PUT `/api/tasks/mark-done/<uuid:id>/`
**Description:** Mark a task as completed.

- **Method:** `PUT`
- **Path Param:** `id` (UUID of the task)
- **Success Response:** `200 OK`
```json
{
  "message": "task marked done"
}
```

- **Failure Response:** `400 Bad Request`
```json
{
  "message": "task marking failed",
  "error": "Reason for failure"
}
```

---

## 🧾 Task Model Overview

```python
class Task(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    task_name = models.CharField(max_length=70)
    task_description = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False, editable=False)
    created_at = models.DateTimeField(editable=False, default=timezone.now)
```

### Field Details:

| Field           | Type       | Description                                      |
|----------------|------------|--------------------------------------------------|
| `id`           | UUID       | Unique identifier (auto-generated)               |
| `task_name`    | CharField  | Title of the task                                |
| `task_description` | CharField | Description or details of the task          |
| `is_completed` | Boolean    | Default always `false`; status whether task is done or not |
| `created_at`   | DateTime   | Timestamp when the task was created              |

---

**Build strong backends — because solid foundations power great software. 💡**