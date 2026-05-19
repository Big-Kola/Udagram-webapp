# Udagram - Setup Guide

---

## Step 1 — Check & Install Prerequisites

Check each tool first. If already installed (version shown), skip the install block.

### 1a. Git

```bash
git --version
```

If not found, install it:

```bash
sudo apt-get install -y git
```

**Docs:** https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

---

### 1b. Node.js & npm

```bash
node --version   # needs v18+
npm --version    # needs v8+
```

If not found or too old, install Node.js v20 (includes npm):

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
node --version
npm --version
```

**Docs:** https://nodejs.org/en/download/package-manager

---

### 1c. PostgreSQL

```bash
psql --version
```

If not found, install it:

```bash
sudo apt-get install -y postgresql postgresql-client
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

**Docs:** https://www.postgresql.org/download/linux/ubuntu/

---

### 1d. curl (for testing API)

```bash
curl --version
```

If not found:

```bash
sudo apt-get install -y curl
```

---

## Step 2 — Initialize Git Repository

```bash
cd /home/big-kola/Udagram-webapp
git init
git add .
git commit -m "Initial commit: Udagram application source code"
```

**Docs:** https://git-scm.com/docs/gittutorial

---

## Step 3 — Configure PostgreSQL Database

```bash
sudo -u postgres psql
```

Inside the psql shell, run:

```sql
CREATE USER postgres WITH PASSWORD 'password';
CREATE DATABASE udagram OWNER postgres;
\q
```

**Docs:** https://www.postgresql.org/docs/current/tutorial-createdb.html

---

## Step 4 — Set Up the Backend API

```bash
cd /home/big-kola/Udagram-webapp/udagram-api
npm install
```

This installs: Express, Sequelize, pg, bcrypt, jsonwebtoken, uuid, multer, TypeScript, etc.

### Run database migrations (creates tables):

```bash
npm run migrate
```

### Start the backend in development mode:

```bash
npm run dev
```

Server starts on **http://localhost:8080**

### Verify:

```bash
curl http://localhost:8080/health
# {"status":"ok"}
```

**Docs:**
- Express: https://expressjs.com/en/guide/routing.html
- Sequelize: https://sequelize.org/docs/v6/getting-started/
- TypeScript: https://www.typescriptlang.org/docs/

---

## Step 5 — Set Up the Frontend

Open a **second terminal**. Check for Ionic CLI first:

```bash
ionic --version
```

If not found, install it globally:

```bash
npm install -g @ionic/cli
```

Then:

```bash
cd /home/big-kola/Udagram-webapp/udagram-frontend
npm install
ionic serve
```

Frontend opens at **http://localhost:8100**

**Docs:**
- Ionic Framework: https://ionicframework.com/docs/
- Angular: https://angular.io/docs

---

## Step 6 — Test the Full Application

### Register a user:

```bash
curl -X POST http://localhost:8080/api/v0/users/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'
```

### Login:

```bash
curl -X POST http://localhost:8080/api/v0/users/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'
```

Save the `token` from the response.

### Create a feed item:

```bash
curl -X POST http://localhost:8080/api/v0/feed \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"caption":"Hello Udagram!","url":"https://picsum.photos/400/300"}'
```

### Get the feed:

```bash
curl http://localhost:8080/api/v0/feed \
  -H "Authorization: Bearer <TOKEN>"
```

**Docs:** https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

---

## Project Structure Reference

```
Udagram-webapp/
├── README.md
├── .gitignore
├── udagram-api/              # Node.js/Express/TypeScript backend
│   ├── package.json
│   ├── tsconfig.json
│   ├── src/
│   │   ├── index.ts          # Server entry point
│   │   ├── server.ts         # Express app + Sequelize connection
│   │   ├── config/config.ts  # Database and JWT config
│   │   └── controllers/v0/
│   │       ├── router.ts     # Route definitions + JWT auth middleware
│   │       ├── feed/         # Feed CRUD endpoints
│   │       └── users/        # Auth endpoints (register/login)
│   └── .sequelizerc
├── udagram-frontend/         # Ionic/Angular frontend
│   ├── package.json
│   ├── ionic.config.json
│   └── src/
│       ├── index.html
│       ├── main.ts
│       ├── app/
│       │   ├── pages/login/  # Login/Register page
│       │   ├── pages/feed/   # Feed page with post creation
│       │   └── services/     # API and Auth services
│       └── environments/     # Environment configs
└── SETUP.md
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `port 5432 already in use` | `sudo service postgresql restart` |
| `Cannot find module` | Run `npm install` in the relevant directory |
| Database connection refused | Ensure PostgreSQL is running: `sudo systemctl status postgresql` |
| `psql: FATAL: password authentication failed` | `sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'password';"` |
| CORS errors | Backend has `cors()` middleware enabled — verify it's imported |
