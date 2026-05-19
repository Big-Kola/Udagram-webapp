# Udagram - Instagram Clone

Udagram is a full-stack Instagram clone application built with a Node.js/Express API backend and an Ionic/Angular frontend.

## Architecture

- **udagram-api** — RESTful API built with Node.js, Express, TypeScript, and PostgreSQL (Sequelize ORM)
- **udagram-frontend** — Mobile-first web app built with Ionic Framework and Angular

## API Endpoints

| Method | Endpoint              | Description          | Auth Required |
|--------|-----------------------|----------------------|---------------|
| GET    | /health               | Health check         | No            |
| POST   | /api/v0/users/login   | Login                | No            |
| POST   | /api/v0/users/register| Register user        | No            |
| GET    | /api/v0/feed          | Get feed items       | Yes           |
| POST   | /api/v0/feed          | Create feed item     | Yes           |
| GET    | /api/v0/feed/:id      | Get feed item by ID  | No            |

## Getting Started

### Prerequisites

- Node.js 18+
- PostgreSQL 14+

### Running Locally

1. Start PostgreSQL and create a database named `udagram`
2. Configure environment variables (see backend config)
3. Install and run the backend:
   ```
   cd udagram-api
   npm install
   npm run dev
   ```
4. Install and run the frontend:
   ```
   cd udagram-frontend
   npm install
   npm start
   ```
