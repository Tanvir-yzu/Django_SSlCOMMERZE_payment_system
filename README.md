# Django Payment Project

This project is a Django-based payment system using SSLCOMMERZ for handling transactions. It includes views for creating payment sessions, handling payment success, failure, and cancellation, as well as IPN (Instant Payment Notification) handling.

## Features

- Create payment sessions with SSLCOMMERZ
- Handle payment success, failure, and cancellation
- Process IPN notifications for transaction validation
- Environment variable configuration for sensitive settings
## Prerequisites
```
pip install sslcommerz-lib
```
- Python 3.x
- Django 3.x or higher
- SSLCOMMERZ account for payment processing

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Django_payment.git
   cd Django_payment
 ```

2. Create a virtual environment:
3. Activate the virtual environment:
   
   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   On macOS/Linux:
4. Install dependencies:
5. Create a .env file in the project root:
6. Run the development server:
7. Access the application:
   
   Open your browser and go to http://127.0.0.1:8000 .
## Project Structure
- Django_payment : Main project directory
  - payment : Django app for payment processing
  - templates : HTML templates for payment views
  - static : Static files (CSS, JavaScript, Images)
  - media : Media files (uploads)
## License
This project is licensed under the MIT License.

## Contact
For any inquiries, please contact [your email address].