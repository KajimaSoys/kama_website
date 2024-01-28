
### Kama Furniture Factory Website Repository README

---

## Introduction
Welcome to the GitHub repository for the Kama Furniture Factory website, accessible at https://kamamebel.com. This site serves as an online catalog showcasing a wide range of soft furniture products, designed to reflect the company's ethos and offerings. While the website facilitates product exploration, it focuses on providing information and connecting customers to the company via messenger for orders.

## Technology Stack
- **Frontend**: Vue.js
- **Backend**: Django
- **Database**: PostgreSQL
- **Containerization**: Docker (Compose)
- **Web Servers**: Nginx
- **Programming Language**: Python, JavaScript

## Features
- **Homepage**: Detailed company description and overview.
- **Additional Pages**: Various informational pages.
- **Product Catalog**: Displaying a range of furniture items.
- **Contact Options**: Messenger integration for order inquiries.

## Installation
To set up the project locally, follow these steps:
1. Clone the repository:
   ```shell
   git clone https://github.com/KajimaSoys/kama_website.git
   ```
2. Navigate to the project directory.
3. Configure `.env` files with the following variables:
   - `DEBUG` - Set for development mode.
   - `SECRET_KEY` - A Django secret key.
   - `ALLOWED_HOSTS` - Default `127.0.0.1,localhost`.
   - `DB_NAME` - Database name.
   - `DB_USER` - Database user.
   - `DB_PASSWORD` - Database password.
   - `DB_HOST` - Default `db`.
   - `DB_PORT` - Default `5432`.
   - `CSRF_COOKIE_SECURE` - Set for HTTPS.
   - `SESSION_COOKIE_SECURE` - Set for HTTPS.
   - `HMAC_KEY` - Key for HMAC.
   - `BITRIX_WEBHOOK_URL` - (Optional) For integrating with Bitrix.

4. Use Docker Compose to build and run the containers:
   ```shell
   docker compose build
   ```
   ```shell
   docker compose up -d
   ```
5. Access the application at `localhost` or the configured port.
