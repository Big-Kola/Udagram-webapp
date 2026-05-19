# Udagram — Local Setup Guide

## 1. Prerequisites

```bash
# Check each — install if missing

node --version          # needs v18+
npm --version           # needs v8+

psql --version          # needs PostgreSQL 14+
sudo systemctl status postgresql   # must be running

curl --version          # for testing the API
```

**Install anything missing:**

```bash
# Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# PostgreSQL
sudo apt-get install -y postgresql postgresql-client
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

---

## 2. Create the Database

```bash
sudo -u postgres psql
```

Inside the psql shell:

```sql
CREATE USER postgres WITH PASSWORD 'password';
CREATE DATABASE udagram OWNER postgres;
\q
```

---

## 3. Run the Backend API

```bash
cd udagram-api
npm install
npm run dev
```

Wait for: `Server running on port 8080`

Verify in another terminal:

```bash
curl http://localhost:8080/health
# → {"status":"ok"}
```

> The app auto-creates tables and seeds a test user (`test@test.com` / `password123`) plus 3 sample feed posts on first run.

---

## 4. Run the Frontend

Open a **second terminal**:

```bash
cd udagram-frontend
npm install
npx @ionic/cli serve
```

Opens at **http://localhost:8100**

> The frontend proxies `/api` requests to `http://localhost:8080` automatically.

---

## 5. Test the API

```bash
# Login as the seeded user
curl -s -X POST http://localhost:8080/api/v0/users/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"password123"}'

# Save the token from the response, then:
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNzc5MTkwMDUzLCJleHAiOjE3Nzk3OTQ4NTN9.DfVMttw6FTsvluPJ0vgzvFVAl-mkrh9MzczIwv0o6DA"

# Get the feed
curl http://localhost:8080/api/v0/feed \
  -H "Authorization: Bearer $TOKEN"

# Create a post
curl -X POST http://localhost:8080/api/v0/feed \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"caption":"My first post!","url":"https://picsum.photos/400/300"}'
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `port 5432 already in use` | `sudo service postgresql restart` |
| `Cannot find module` | Run `npm install` in the relevant directory |
| Database connection refused | `sudo systemctl status postgresql` — make sure it's active |
| `password authentication failed` | `sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'password';"` |
| `ionic: command not found` | Use `npx @ionic/cli serve` instead |
