from fpdf import FPDF
import os

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", uni=True)
        self.add_font("DejaVu", "B", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", uni=True)
        self.add_font("DejaVu", "I", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", uni=True)
        self.add_font("DejaVuMono", "", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", uni=True)
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        if self.page_no() > 1:
            self.set_font("DejaVu", "I", 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 8, "Udagram - Complete Project Guide", align="C")
            self.ln(5)
            self.set_draw_color(200, 200, 200)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def title1(self, text):
        self.set_font("DejaVu", "B", 18)
        self.set_text_color(25, 60, 120)
        self.cell(0, 12, text, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(25, 60, 120)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def title2(self, text):
        self.set_font("DejaVu", "B", 14)
        self.set_text_color(50, 90, 150)
        self.cell(0, 10, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def title3(self, text):
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(70, 70, 70)
        self.cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def paragraph(self, text):
        self.set_font("DejaVu", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text, indent=15):
        x = self.get_x()
        self.set_font("DejaVu", "", 10)
        self.set_text_color(30, 30, 30)
        self.set_x(x + indent)
        self.cell(4, 5.5, chr(8226))
        self.multi_cell(0, 5.5, text)
        self.ln(0.5)

    def code_block(self, text):
        self.set_font("DejaVuMono", "", 8)
        self.set_text_color(20, 20, 20)
        self.set_fill_color(240, 240, 245)
        self.set_draw_color(200, 200, 210)
        y_before = self.get_y()
        self.multi_cell(0, 4.5, text, fill=True)
        self.set_draw_color(200, 200, 210)
        self.line(10, y_before, 200, y_before)
        self.ln(3)

    def table(self, headers, rows, col_widths=None):
        self.set_font("DejaVu", "B", 9)
        self.set_fill_color(25, 60, 120)
        self.set_text_color(255, 255, 255)
        if col_widths is None:
            col_widths = [180 / len(headers)] * len(headers)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, h, border=1, fill=True, align="C")
        self.ln()
        self.set_font("DejaVu", "", 8.5)
        self.set_text_color(30, 30, 30)
        fill = False
        for row in rows:
            if self.get_y() > 270:
                self.add_page()
                self.set_font("DejaVu", "B", 9)
                self.set_fill_color(25, 60, 120)
                self.set_text_color(255, 255, 255)
                for i, h in enumerate(headers):
                    self.cell(col_widths[i], 7, h, border=1, fill=True, align="C")
                self.ln()
                self.set_font("DejaVu", "", 8.5)
                self.set_text_color(30, 30, 30)
            if fill:
                self.set_fill_color(245, 245, 250)
            else:
                self.set_fill_color(255, 255, 255)
            for i, cell_text in enumerate(row):
                self.cell(col_widths[i], 6, str(cell_text), border=1, fill=True, align="C" if i == 0 else "L")
            self.ln()
            fill = not fill
        self.ln(3)


def build_pdf():
    pdf = PDF()
    pdf.alias_nb_pages()

    # ==================== COVER PAGE ====================
    pdf.add_page()
    pdf.ln(50)
    pdf.set_font("DejaVu", "B", 32)
    pdf.set_text_color(25, 60, 120)
    pdf.cell(0, 15, "UDAGRAM", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DejaVu", "", 16)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 10, "Instagram Clone - Full Project Guide", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    pdf.set_font("DejaVu", "I", 11)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 8, "A complete walkthrough for beginners", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, "from development to AWS deployment", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(30)

    # Table of Contents placeholder
    pdf.set_font("DejaVu", "B", 14)
    pdf.set_text_color(25, 60, 120)
    pdf.cell(0, 10, "TABLE OF CONTENTS", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    toc = [
        "1.  Project Overview & Aim",
        "2.  Architecture Overview",
        "3.  Technology Stack - Why Each Tool Was Chosen",
        "4.  Architecture Diagram",
        "5.  Project Structure (File-by-File)",
        "6.  Backend API - Deep Dive",
        "7.  Frontend App - Deep Dive",
        "8.  Infrastructure (Terraform) - Resource-by-Resource",
        "9.  Step-by-Step: Run Locally",
        "10. Step-by-Step: Deploy to AWS",
        "11. Cost Analysis & Necessity of Each Resource",
        "12. Common Issues & Troubleshooting",
        "13. How to Extend the Project",
    ]
    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(60, 60, 60)
    for item in toc:
        pdf.cell(0, 7, f"     {item}", new_x="LMARGIN", new_y="NEXT")

    # ==================== SECTION 1: PROJECT OVERVIEW ====================
    pdf.add_page()
    pdf.title1("1. PROJECT OVERVIEW & AIM")

    pdf.title2("What is Udagram?")
    pdf.paragraph(
        "Udagram is a full-stack web application that mimics the core functionality of Instagram. "
        "Users can register an account, log in, view a feed of image posts, and create new posts "
        "by providing a caption and an image URL. It is built as a learning project to demonstrate "
        "modern cloud-native application development and deployment."
    )

    pdf.title2("Project Aim")
    pdf.paragraph(
        "The primary goal of Udagram is to serve as a hands-on educational project that covers "
        "the entire lifecycle of a modern web application:"
    )
    pdf.bullet("Building a RESTful API with Node.js, Express, TypeScript, and PostgreSQL")
    pdf.bullet("Creating a mobile-first frontend with Ionic Framework and Angular")
    pdf.bullet("Containerizing applications with Docker")
    pdf.bullet("Deploying to AWS using Infrastructure as Code (Terraform)")
    pdf.bullet("Using cloud services: VPC, ECS Fargate, RDS, ALB, CloudWatch")
    pdf.bullet("Implementing authentication with JWT tokens")

    pdf.title2("Who Is This For?")
    pdf.paragraph(
        "This guide is written for beginners who have basic programming knowledge (JavaScript, "
        "command line) but want to understand how to build and deploy a complete full-stack "
        "application on AWS. By the end, you will understand every file, every configuration, "
        "and every cloud resource in this project."
    )

    # ==================== SECTION 2: ARCHITECTURE OVERVIEW ====================
    pdf.add_page()
    pdf.title1("2. ARCHITECTURE OVERVIEW")

    pdf.paragraph(
        "Udagram follows a standard three-tier architecture pattern:"
    )

    pdf.table(
        ["Tier", "Technology", "Description"],
        [
            ["Frontend", "Ionic / Angular", "Mobile-first SPA served by Nginx inside Docker"],
            ["Backend API", "Node.js / Express", "REST API with JWT auth, served on port 8080"],
            ["Database", "PostgreSQL", "Relational database storing users and feed posts"],
        ],
        [40, 55, 85],
    )

    pdf.paragraph(
        "In the local development setup, all three tiers run on your machine (or via Docker Compose). "
        "In the AWS deployment, the frontend and backend each run as Docker containers in ECS Fargate, "
        "the database runs on RDS, and an Application Load Balancer (ALB) routes traffic between them."
    )

    pdf.title2("Request Flow (AWS Deployment)")
    pdf.paragraph(
        "1. User opens http://app-lb-... in their browser\n"
        "2. The ALB receives the request on port 80\n"
        "3. If the path is /api/*, the ALB forwards to the backend ECS tasks (port 8080)\n"
        "4. If the path is anything else (e.g., / or /feed), the ALB forwards to the frontend ECS tasks (port 80)\n"
        "5. The frontend (Angular SPA) loads and the Angular router handles client-side routes\n"
        "6. When the feed page loads, it calls GET /api/v0/feed via the ALB\n"
        "7. The backend queries PostgreSQL and returns JSON feed data\n"
        "8. The frontend renders images from the URLs in the response (external URLs like picsum.photos)"
    )

    # ==================== SECTION 3: TECHNOLOGY STACK ====================
    pdf.add_page()
    pdf.title1("3. TECHNOLOGY STACK - WHY EACH TOOL WAS CHOSEN")

    technologies = [
        ("Node.js", "The runtime for our backend. Chosen because it uses JavaScript (same language as the frontend), has a massive ecosystem (npm), and is excellent for I/O-heavy web applications. Non-blocking event loop makes it perfect for handling many API requests."),
        ("Express", "The most popular web framework for Node.js. Minimal, unopinionated, and extremely well-documented. Makes it easy to define routes, middleware, and handle HTTP requests/responses."),
        ("TypeScript", "Adds static types to JavaScript. Catches bugs at compile time, provides better IDE support, and makes the code more maintainable. Essential for any non-trivial project."),
        ("PostgreSQL", "A powerful, open-source relational database. Chosen over NoSQL for this project because user accounts and feed posts have clear relationships. Supports advanced features like JSON fields if needed later."),
        ("Sequelize", "An ORM (Object-Relational Mapper) for Node.js. Lets you interact with PostgreSQL using JavaScript objects instead of raw SQL. Handles migrations, model definitions, and query building."),
        ("Ionic Framework", "A mobile-first UI framework built on Angular. Provides beautiful, native-like UI components (cards, headers, inputs). Makes the app look good on both mobile and desktop without custom CSS."),
        ("Angular", "A full-featured frontend framework. Chosen because it provides routing, HTTP client, forms, and dependency injection out of the box. More structured than React, which is good for beginners learning patterns."),
        ("Docker", "Containerizes the application so it runs the same everywhere. Eliminates 'it works on my machine' problems. The backend and frontend each have a Dockerfile."),
        ("Docker Compose", "Orchestrates multi-container local development. With one command (docker-compose up), you get PostgreSQL, the API, and the frontend all running together."),
        ("Terraform", "Infrastructure as Code tool. Defines ALL AWS resources in declarative configuration files. Makes the infrastructure reproducible, version-controlled, and destroyable with one command."),
        ("AWS ECS Fargate", "Serverless container orchestration. You define the container (CPU, memory, image) and AWS runs it for you. No servers to manage. Auto-heals failed tasks."),
        ("AWS ALB", "Application Load Balancer. Distributes traffic across multiple ECS tasks. Routes /api/* to backend and everything else to frontend. Performs health checks."),
        ("AWS RDS", "Managed PostgreSQL. AWS handles backups, patching, and replication. Much easier than running PostgreSQL on a server yourself."),
        ("JWT (JSON Web Tokens)", "Stateless authentication. When a user logs in, the server signs a token containing their user info. The client sends this token with each request. No server-side session storage needed."),
        ("bcryptjs", "Password hashing library. Stores hashed passwords, not plain text. The bcrypt algorithm is intentionally slow to resist brute-force attacks."),
    ]

    pdf.set_font("DejaVu", "", 9.5)
    pdf.set_text_color(30, 30, 30)
    for name, desc in technologies:
        pdf.set_font("DejaVu", "B", 10)
        pdf.set_text_color(25, 60, 120)
        pdf.cell(0, 6, name, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("DejaVu", "", 9.5)
        pdf.set_text_color(30, 30, 30)
        pdf.multi_cell(0, 5, desc)
        pdf.ln(2)

    # ==================== SECTION 4: ARCHITECTURE DIAGRAM ====================
    pdf.add_page()
    pdf.title1("4. ARCHITECTURE DIAGRAM")

    pdf.paragraph(
        "Below is the architecture diagram for the AWS deployment. Each box represents "
        "an AWS resource or application component, and arrows show the flow of traffic."
    )

    pdf.title2("AWS Deployment Architecture")

    # Simple diagram using text boxes
    # We'll draw it with rectangles and lines using fpdf's drawing capabilities

    pdf.set_draw_color(25, 60, 120)
    pdf.set_line_width(0.5)

    def draw_box(x, y, w, h, title, subtitle="", fill_color=(230, 240, 255), text_color=(20, 20, 80)):
        pdf.set_fill_color(*fill_color)
        pdf.set_draw_color(25, 60, 120)
        pdf.rect(x, y, w, h, style="DF")
        pdf.set_font("DejaVu", "B", 10)
        pdf.set_text_color(*text_color)
        pdf.set_xy(x, y + 3)
        pdf.cell(w, 7, title, align="C", new_x="LMARGIN", new_y="NEXT")
        if subtitle:
            pdf.set_font("DejaVu", "", 7)
            pdf.set_text_color(80, 80, 80)
            pdf.set_xy(x, y + 11)
            pdf.cell(w, 5, subtitle, align="C")

    def draw_arrow(x1, y1, x2, y2, label=""):
        pdf.set_draw_color(60, 60, 60)
        pdf.set_line_width(0.3)
        pdf.line(x1, y1, x2, y2)
        # arrow head
        dx = x2 - x1
        dy = y2 - y1
        angle = 0.5  # ~30 degrees
        arrow_len = 4
        nx = dx / (dx*dx + dy*dy)**0.5 if (dx*dx + dy*dy) > 0 else 0
        ny = dy / (dx*dx + dy*dy)**0.5 if (dx*dx + dy*dy) > 0 else 0
        ax1 = x2 - arrow_len * (nx * 0.866 - ny * 0.5)
        ay1 = y2 - arrow_len * (ny * 0.866 + nx * 0.5)
        ax2 = x2 - arrow_len * (nx * 0.866 + ny * 0.5)
        ay2 = y2 - arrow_len * (ny * 0.866 - nx * 0.5)
        pdf.line(x2, y2, ax1, ay1)
        pdf.line(x2, y2, ax2, ay2)
        if label:
            pdf.set_font("DejaVu", "I", 7)
            pdf.set_text_color(80, 80, 80)
            pdf.set_xy((x1+x2)/2 - 10, (y1+y2)/2 - 3)
            # pdf.cell(20, 5, label, align="C")

    start_y = 35
    box_w = 55
    box_h = 20

    # Row 1: User / Browser
    draw_box(72, start_y, 55, 18, "User Browser", "Chrome / Firefox / Safari")

    # Arrow from User to ALB
    draw_arrow(100, start_y + 18, 100, start_y + 50)

    # Row 2: ALB
    draw_box(72, start_y + 50, 55, 20, "ALB (port 80)", "Application Load Balancer")

    # Arrow from ALB to Frontend
    draw_arrow(72, start_y + 60, 40, start_y + 100)

    # Arrow from ALB to Backend
    draw_arrow(100, start_y + 70, 100, start_y + 110)
    pdf.set_font("DejaVu", "I", 7)
    pdf.set_text_color(80, 80, 80)
    pdf.set_xy(80, start_y + 92)
    pdf.cell(20, 5, "/api/*")

    # Arrow from Frontend route
    draw_arrow(160, start_y + 60, 160, start_y + 100)
    pdf.set_font("DejaVu", "I", 7)
    pdf.set_text_color(80, 80, 80)
    pdf.set_xy(140, start_y + 75)
    pdf.cell(20, 5, "/* (default)")

    # Row 3 left: Frontend ECS
    draw_box(12, start_y + 100, 55, 22, "Frontend ECS", "Nginx + Angular SPA", fill_color=(230, 255, 230), text_color=(20, 80, 20))

    # Row 3 center: Backend ECS
    draw_box(72, start_y + 110, 55, 22, "Backend ECS", "Express API (port 8080)", fill_color=(255, 240, 230), text_color=(80, 50, 20))

    # Row 3 right: (placeholder for balance)
    draw_box(132, start_y + 100, 55, 22, "Backend ECS", "Express API (port 8080)", fill_color=(255, 240, 230), text_color=(80, 50, 20))

    # Arrow from Backend to DB
    draw_arrow(100, start_y + 132, 100, start_y + 170)

    # Row 4: RDS
    draw_box(60, start_y + 170, 80, 20, "RDS PostgreSQL", "db.t4g.micro", fill_color=(255, 255, 230), text_color=(80, 80, 20))

    pdf.ln(start_y + 200)

    pdf.title2("Local Development Architecture (Docker Compose)")
    pdf.paragraph(
        "When running locally with docker-compose, the architecture is simpler:"
    )
    pdf.bullet("db: PostgreSQL 14 container (port 5432)")
    pdf.bullet("api: Express backend container (port 8080), connects to db")
    pdf.bullet("frontend: Nginx + Angular container (port 80), communicates with api via HTTP")

    # ==================== SECTION 5: PROJECT STRUCTURE ====================
    pdf.add_page()
    pdf.title1("5. PROJECT STRUCTURE (FILE-BY-FILE)")

    pdf.paragraph(
        "Here is every file in the project with a plain-English explanation of what it does."
    )

    pdf.title2("Root Directory")
    pdf.table(
        ["File", "Purpose"],
        [
            ["README.md", "Brief project overview and quick start instructions"],
            ["SETUP.md", "Detailed step-by-step local setup guide"],
            ["DEPLOY_AWS.md", "Full AWS deployment guide with Terraform"],
            ["docker-compose.yml", "Defines 3 services: db, api, frontend for local dev"],
            [".gitignore", "Tells git which files to ignore (node_modules, dist, .terraform, etc.)"],
            [".dockerignore", "Prevents node_modules being copied into Docker images"],
        ],
        [55, 125],
    )

    pdf.title2("terraform/ - Infrastructure as Code")
    pdf.table(
        ["File", "Purpose"],
        [
            ["main.tf", "ALL infrastructure resources: VPC, subnets, ALB, ECS, RDS, IAM, etc."],
            ["variables.tf", "Input variables (region, passwords, image names)"],
            ["output.tf", "Outputs displayed after terraform apply (ALB DNS, RDS endpoint, etc.)"],
            ["terraform.tfvars", "Actual values for the variables (your AWS region, passwords)"],
            ["terraform.tfstate", "State file - tracks what Terraform has created (DO NOT EDIT)"],
        ],
        [55, 125],
    )

    pdf.title2("udagram-api/ - Backend API")
    pdf.table(
        ["File / Directory", "Purpose"],
        [
            ["src/server.ts", "Express app setup, CORS, body parser, health endpoint, Sequelize connection"],
            ["src/index.ts", "Entry point: connects DB, syncs tables, seeds data, starts server"],
            ["src/config/config.ts", "Reads env vars for DB, JWT secret with default fallbacks"],
            ["src/controllers/v0/router.ts", "Mounts feed router at /feed and user router at /users"],
            ["src/controllers/v0/feed/FeedController.ts", "GET/POST /feed endpoints + GET /feed/:id"],
            ["src/controllers/v0/feed/FeedModel.ts", "FeedItem Sequelize model (caption + url fields)"],
            ["src/controllers/v0/users/UserController.ts", "POST /register and POST /login endpoints"],
            ["src/controllers/v0/users/UserModel.ts", "User Sequelize model with bcrypt password hashing"],
            ["src/controllers/v0/middleware/auth.ts", "JWT verification middleware for protected routes"],
            ["Dockerfile", "Builds the TypeScript and runs the compiled API on Node.js 18"],
            ["package.json", "Dependencies and scripts (dev, build, start)"],
            ["tsconfig.json", "TypeScript compiler settings"],
        ],
        [55, 125],
    )

    pdf.title2("udagram-frontend/ - Frontend App")
    pdf.table(
        ["File / Directory", "Purpose"],
        [
            ["src/index.html", "Root HTML file that loads the Angular app"],
            ["src/main.ts", "Angular bootstrap file - starts the app"],
            ["src/environments/environment.ts", "Dev config: apiUrl = /api/v0"],
            ["src/environments/environment.prod.ts", "Prod config: reads __env__ or falls back to /api/v0"],
            ["src/app/app.module.ts", "Angular root module - imports all features"],
            ["src/app/app-routing.module.ts", "Routes: / -> /feed, /login, /feed"],
            ["src/app/pages/login/login.page.ts", "Login/Register form logic"],
            ["src/app/pages/login/login.page.html", "Login page template with Ionic inputs"],
            ["src/app/pages/feed/feed.page.ts", "Feed page - loads posts, creates new posts"],
            ["src/app/pages/feed/feed.page.html", "Feed page template with card list and form"],
            ["src/app/services/api.service.ts", "HTTP calls to the backend API"],
            ["src/app/services/auth.service.ts", "JWT token management in localStorage"],
            ["Dockerfile", "Multi-stage build: Node builds Angular, Nginx serves it"],
            ["nginx.conf", "Nginx config: serves index.html for all routes (SPA fallback)"],
        ],
        [55, 125],
    )

    # ==================== SECTION 6: BACKEND DEEP DIVE ====================
    pdf.add_page()
    pdf.title1("6. BACKEND API - DEEP DIVE")

    pdf.title2("server.ts - The Express App (Line by Line)")
    pdf.code_block(
        "import express from 'express';\n"
        "import cors from 'cors';\n"
        "import bodyParser from 'body-parser';\n"
        "import { Sequelize } from 'sequelize';\n"
        "import { config } from './config/config';"
    )
    pdf.paragraph(
        "Imports the Express framework (handles HTTP routing), CORS (allows cross-origin requests "
        "from the frontend), body-parser (reads JSON from request bodies), and Sequelize (connects "
        "to PostgreSQL)."
    )

    pdf.code_block(
        "const app = express();\n"
        "app.use(cors({ origin: '*' }));\n"
        "app.use(bodyParser.json());"
    )
    pdf.paragraph(
        "Creates the Express app and adds middleware. CORS is set to '*' (allow all origins) - "
        "this is fine for a learning project but should be restricted in production. bodyParser.json() "
        "automatically parses incoming JSON request bodies."
    )

    pdf.code_block(
        "app.get('/', (req, res) => res.json({ name: 'Udagram API', version: '1.0.0', ... }));\n"
        "app.get('/health', (req, res) => res.send({ status: 'ok' }));"
    )
    pdf.paragraph(
        "Two simple endpoints. The root endpoint returns API info (useful for checking the API is alive). "
        "The /health endpoint is used by the ALB to check if the backend is healthy - the target group "
        "is configured to check /health every 30 seconds."
    )

    pdf.title2("index.ts - Application Entry Point")
    pdf.paragraph(
        "This is where the application starts. Here's the flow:"
    )
    pdf.bullet("1. The Sequelize connection authenticates (checks DB credentials are correct)")
    pdf.bullet("2. Tables are synced (created if they don't exist). In development, force: true drops and recreates tables. In production (NODE_ENV=production), it only creates missing tables without dropping.")
    pdf.bullet("3. The seed function checks if any users exist. If not, it creates a test user (test@test.com / password123) and 3 sample feed posts with images from picsum.photos")
    pdf.bullet("4. Routes are mounted at /api/v0")
    pdf.bullet("5. The server starts listening on PORT (default 8080)")

    pdf.title2("FeedController.ts - The Feed API")
    pdf.paragraph("Three endpoints control the feed:")
    pdf.code_block(
        "GET /feed      -> Returns all feed items (no auth required)\n"
        "POST /feed     -> Creates a new post (auth required via requireAuth middleware)\n"
        "GET /feed/:id  -> Returns a single post by ID (no auth required)"
    )
    pdf.paragraph(
        "The GET endpoints are intentionally left without authentication so you can test them with curl "
        "without needing a token. The POST endpoint requires authentication because only logged-in users "
        "should be able to create posts."
    )

    pdf.title2("UserController.ts - Authentication")
    pdf.code_block(
        "POST /register -> Creates a user, hashes password with bcrypt, returns JWT token\n"
        "POST /login    -> Validates email + password, returns JWT token"
    )
    pdf.paragraph(
        "When a user registers, their password is hashed with bcrypt (10 salt rounds) before storing. "
        "When logging in, the provided password is compared against the stored hash. If valid, a JWT "
        "token is signed containing the user's id and email, with an expiration of 7 days. The client "
        "stores this token and sends it with every authenticated request as Authorization: Bearer <token>."
    )

    pdf.title2("auth.ts - JWT Middleware")
    pdf.paragraph(
        "The requireAuth function checks the Authorization header, extracts the Bearer token, "
        "verifies it with the JWT secret, and attaches the decoded user info to the request. "
        "If the token is missing, expired, or invalid, it returns a 401 error with a helpful message."
    )

    pdf.title2("Sequelize Models")
    pdf.paragraph(
        "FeedItem model has: id (auto-increment), caption (string, max 256 chars), url (string, max 512 chars), "
        "createdAt and updatedAt (auto-managed by Sequelize). The table is named 'feed'.\n\n"
        "User model has: id (auto-increment), email (string, unique), passwordHash (string), "
        "createdAt and updatedAt. The table is named 'users'. It also has class methods "
        "hashPassword (bcrypt) and instance method validatePassword."
    )

    # ==================== SECTION 7: FRONTEND DEEP DIVE ====================
    pdf.add_page()
    pdf.title1("7. FRONTEND APP - DEEP DIVE")

    pdf.title2("Architecture Pattern")
    pdf.paragraph(
        "The frontend is a Single Page Application (SPA) built with Angular 15 and Ionic 6. "
        "The Nginx server serves the compiled static files and handles client-side routing by "
        "returning index.html for all routes (the 'SPA fallback' pattern)."
    )

    pdf.title2("AppModule & Routing")
    pdf.paragraph(
        "app.module.ts imports BrowserModule, FormsModule (for ngModel two-way binding), "
        "HttpClientModule (for HTTP requests), IonicModule (for UI components), and the "
        "AppRoutingModule (which defines routes).\n\n"
        "There are 3 routes:\n"
        "  / (empty path) -> redirects to /feed\n"
        "  /login        -> loads LoginPageModule (lazy loaded)\n"
        "  /feed         -> loads FeedPageModule (lazy loaded)\n\n"
        "Lazy loading means the login and feed code is only loaded when you visit those pages, "
        "making the initial load faster."
    )

    pdf.title2("Authentication Flow")
    pdf.paragraph(
        "1. User navigates to /feed\n"
        "2. FeedPage.ngOnInit() checks AuthService.isLoggedIn()\n"
        "3. If not logged in, redirects to /login\n"
        "4. User enters email + password and clicks submit\n"
        "5. LoginPage calls ApiService.login() which POSTs to /api/v0/users/login\n"
        "6. The backend validates credentials and returns a JWT token\n"
        "7. AuthService.setToken() stores the token in localStorage\n"
        "8. Router navigates to /feed\n"
        "9. FeedPage.loadFeed() calls ApiService.getFeed(token) which GETs /api/v0/feed\n"
        "10. The response is an array of feed items with caption, url, createdAt fields\n"
        "11. The HTML template renders an <img> tag for each item's url"
    )

    pdf.title2("AuthService")
    pdf.code_block(
        "setToken(token) -> localStorage.setItem('udagram_token', token)\n"
        "getToken()      -> localStorage.getItem('udagram_token')\n"
        "isLoggedIn()    -> returns true if token exists\n"
        "logout()        -> localStorage.removeItem('udagram_token')"
    )
    pdf.paragraph(
        "The token is stored in the browser's localStorage. This is a simple approach suitable "
        "for learning projects. For production, you'd want to consider XSS vulnerabilities and "
        "use httpOnly cookies instead."
    )

    pdf.title2("Environment Configuration")
    pdf.paragraph(
        "environment.ts (development) sets apiUrl to '/api/v0'. This means API calls go to the "
        "same origin (e.g., http://localhost:8100/api/v0/feed during local dev). During local dev "
        "with 'ionic serve', the Ionic CLI proxies /api requests to http://localhost:8080.\n\n"
        "environment.prod.ts (production) reads from window.__env__.apiUrl if available, otherwise "
        "falls back to '/api/v0'. The __env__ object would be injected at runtime by a startup "
        "script if you need dynamic configuration.\n\n"
        "IMPORTANT: The Dockerfile runs 'ionic build' WITHOUT --prod, so the development environment "
        "file is used in the production Docker image as well!"
    )

    pdf.title2("Nginx Configuration")
    pdf.code_block(
        "server {\n"
        "  listen 80;\n"
        "  root /usr/share/nginx/html;\n"
        "  index index.html;\n"
        "  location / { try_files $uri $uri/ /index.html; }\n"
        "}"
    )
    pdf.paragraph(
        "This is the standard SPA configuration. For any request, Nginx first tries to serve the "
        "exact file ($uri), then tries it as a directory ($uri/), and if neither exists, serves "
        "index.html. This allows Angular to handle client-side routing (e.g., /feed) even though "
        "no actual feed.html file exists on the server."
    )

    # ==================== SECTION 8: TERRAFORM DEEP DIVE ====================
    pdf.add_page()
    pdf.title1("8. INFRASTRUCTURE (TERRAFORM) - RESOURCE-BY-RESOURCE")

    pdf.paragraph(
        "This section explains every Terraform resource, why it was used, and whether it's "
        "strictly necessary. Resources are organized by category."
    )

    pdf.title2("Networking Layer")
    pdf.table(
        ["Resource", "Why It Exists", "Necessary?"],
        [
            ["aws_vpc", "Creates an isolated network in AWS. All other resources live inside it.", "YES - required"],
            ["aws_subnet (6)", "Divides VPC into segments: 2 public (for ALB), 2 private backend (for ECS), 2 private database (for RDS). Public subnets have internet access; private don't.", "YES - proper networking"],
            ["aws_internet_gateway", "Allows internet traffic to reach the public subnets (and the ALB).", "YES - ALB needs internet"],
            ["aws_eip (2)", "Elastic IPs for NAT Gateways. Static public IPs that don't change.", "YES - NAT needs fixed IP"],
            ["aws_nat_gateway (2)", "Allows ECS tasks in private subnets to download Docker images, access ECR, etc., without being directly internet-accessible.", "YES - private subnets need outbound"],
            ["aws_route_table (3)", "Public route table (traffic -> IGW), private per AZ (traffic -> NAT). Defines how traffic flows out of each subnet.", "YES - required"],
            ["aws_route_table_association (6)", "Links each subnet to a route table.", "YES - required"],
            ["aws_db_subnet_group", "Groups the 2 database subnets so RDS knows which subnets to use.", "YES - RDS requires it"],
        ],
        [40, 110, 30],
    )

    pdf.title2("Security Layer")
    pdf.table(
        ["Resource", "Why It Exists", "Necessary?"],
        [
            ["aws_security_group.alb_sg", "ALB security group: allows inbound HTTP (80) from the internet (0.0.0.0/0). Allows outbound to anywhere (to forward to ECS).", "YES - critical for security"],
            ["aws_security_group.backend_sg", "Backend security: allows inbound on port 8080 ONLY from the ALB (not from the internet directly). This is defense-in-depth.", "YES - critical for security"],
            ["aws_security_group.db_sg", "Database security: allows inbound on port 5432 ONLY from the backend security group. The database is completely isolated from direct access.", "YES - critical for security"],
            ["aws_security_group.frontend_sg", "Frontend security: allows inbound on port 80 ONLY from the ALB.", "YES - critical for security"],
        ],
        [40, 110, 30],
    )

    pdf.title2("Application Layer")
    pdf.table(
        ["Resource", "Why It Exists", "Necessary?"],
        [
            ["aws_lb (ALB)", "Application Load Balancer. Accepts traffic on port 80 and distributes it across healthy ECS tasks. Routes /api/* to backend, everything else to frontend.", "YES - required for scaling HA"],
            ["aws_lb_listener", "Configures the ALB's port 80 listener. Defines the default action (forward to frontend) and the path-based rule (forward /api/* to backend).", "YES - required"],
            ["aws_lb_listener_rule", "The path-based routing rule that sends /api/* requests to the backend target group.", "YES - separates frontend/backend"],
            ["aws_lb_target_group (2)", "1 for frontend (port 80, health check on /), 1 for backend (port 8080, health check on /health). Each registers healthy ECS task IPs.", "YES - required"],
            ["aws_ecs_cluster", "The ECS cluster that groups our Fargate services. With container insights enabled.", "YES - required"],
            ["aws_ecs_task_definition (2)", "Defines what container to run: frontend (256 CPU, 512MB, image = frontend_image) and backend (512 CPU, 1024MB, image = backend_image with env vars).", "YES - required"],
            ["aws_ecs_service (2)", "Runs 2 copies (desired_count=2) of each task in Fargate, attached to the ALB.", "YES - required"],
        ],
        [40, 110, 30],
    )

    pdf.title2("Data Layer")
    pdf.table(
        ["Resource", "Why It Exists", "Necessary?"],
        [
            ["aws_db_instance (RDS)", "Managed PostgreSQL 14, db.t4g.micro (1 CPU, 1GB RAM, 20GB gp3 storage). AWS handles backups, patching, and monitoring.", "YES - required for data"],
        ],
        [40, 110, 30],
    )

    pdf.title2("IAM & Monitoring")
    pdf.table(
        ["Resource", "Why It Exists", "Necessary?"],
        [
            ["aws_iam_role (2)", "ecs_execution_role: allows ECS to pull images and send logs. ecs_task_role: allows the container to call AWS APIs (if needed for future features).", "YES - ECS requires roles"],
            ["aws_iam_role_policy_attachment (2)", "Attaches AmazonECSTaskExecutionRolePolicy and CloudWatchLogsFullAccess to the execution role.", "YES - required permissions"],
            ["aws_cloudwatch_log_group", "Stores container logs from ECS. /ecs/udagram-backend, 30-day retention. Each container sends stdout/stderr here.", "YES - essential for debugging"],
        ],
        [40, 110, 30],
    )

    # ==================== SECTION 9: RUN LOCALLY ====================
    pdf.add_page()
    pdf.title1("9. STEP-BY-STEP: RUN LOCALLY")

    pdf.title2("Prerequisites")
    pdf.bullet("Node.js 18+")
    pdf.bullet("Docker and Docker Compose")
    pdf.bullet("Git")
    pdf.bullet("A terminal / command prompt")

    pdf.title2("Method A: Docker Compose (Easiest)")
    pdf.paragraph("This runs everything in containers with one command:")
    pdf.code_block(
        "# Clone the repository\n"
        "git clone <repo-url> udagram-webapp\n"
        "cd udagram-webapp\n\n"
        "# Start all services (PostgreSQL + API + Frontend)\n"
        "docker-compose up --build\n\n"
        "# Open http://localhost in your browser\n"
        "# Login with: test@test.com / password123"
    )
    pdf.paragraph(
        "Docker Compose starts 3 containers. The db container runs PostgreSQL with a health check. "
        "The api container waits for db to be healthy, then starts. The frontend container waits "
        "for api to be ready. The API auto-creates tables and seeds the test user + 3 sample posts."
    )

    pdf.title2("Method B: Running Natively (Without Docker)")
    pdf.paragraph("Step 1: Set up PostgreSQL")
    pdf.code_block(
        "# On Ubuntu/Debian:\n"
        "sudo apt-get install -y postgresql postgresql-client\n"
        "sudo systemctl start postgresql\n\n"
        "# Create the database:\n"
        "sudo -u postgres psql -c \"CREATE USER postgres WITH PASSWORD 'password';\"\n"
        "sudo -u postgres psql -c \"CREATE DATABASE udagram OWNER postgres;\""
    )

    pdf.paragraph("Step 2: Start the Backend API")
    pdf.code_block(
        "cd udagram-api\n"
        "npm install\n"
        "npm run dev\n\n"
        "# Expected output:\n"
        "# Database connected\n"
        "# Tables synced (force=true)\n"
        "# Seeded test user: test@test.com / password123\n"
        "# Seeded 3 sample feed items\n"
        "# Server running on port 8080"
    )

    pdf.paragraph("Step 3: Start the Frontend")
    pdf.code_block(
        "cd udagram-frontend\n"
        "npm install\n"
        "npx @ionic/cli serve\n\n"
        "# Opens at http://localhost:8100"
    )

    pdf.title2("Testing the API with curl")
    pdf.code_block(
        "# Health check\n"
        "curl http://localhost:8080/health\n\n"
        "# Login\n"
        "curl -s -X POST http://localhost:8080/api/v0/users/login \\\n"
        "  -H \"Content-Type: application/json\" \\\n"
        "  -d '{\"email\":\"test@test.com\",\"password\":\"password123\"}'\n\n"
        "# Save the token, then:\n"
        "# Get feed\n"
        "curl http://localhost:8080/api/v0/feed \\\n"
        "  -H \"Authorization: Bearer <TOKEN>\""
    )

    # ==================== SECTION 10: DEPLOY TO AWS ====================
    pdf.add_page()
    pdf.title1("10. STEP-BY-STEP: DEPLOY TO AWS")

    pdf.title2("Prerequisites")
    pdf.bullet("AWS account with appropriate permissions")
    pdf.bullet("AWS CLI installed and configured (aws configure)")
    pdf.bullet("Terraform >= 1.5")
    pdf.bullet("Docker")
    pdf.bullet("Node.js >= 18")

    pdf.title2("Step 1: Configure Infrastructure Variables")
    pdf.code_block(
        "# Edit terraform/terraform.tfvars with your values:\n"
        "aws_region       = \"us-east-1\"\n"
        "db_password      = \"your-strong-password\"\n"
        "jwt_secret       = \"your-random-secret\"\n"
        "backend_image    = \"your-dockerhub-username/udagram-api:latest\"\n"
        "frontend_image   = \"your-dockerhub-username/udagram-frontend:latest\""
    )
    pdf.paragraph(
        "The backend_image and frontend_image are Docker image names that Terraform will use "
        "in the ECS task definitions. You need to push these images to a container registry "
        "(Docker Hub, ECR, etc.) before Terraform can use them."
    )

    pdf.title2("Step 2: Apply Terraform")
    pdf.code_block(
        "cd terraform\n"
        "terraform init\n"
        "terraform plan\n"
        "terraform apply -auto-approve\n\n"
        "# This will create ALL AWS resources. It takes ~5-10 minutes.\n"
        "# After completion, note the outputs:\n"
        "# alb_dns = app-lb-XXXXXXXXXX.us-east-1.elb.amazonaws.com\n"
        "# rds_endpoint = udagram-db.XXXXXXXXXX.us-east-1.rds.amazonaws.com"
    )

    pdf.title2("Step 3: Build and Push Docker Images")
    pdf.code_block(
        "# Build and push backend\n"
        "cd udagram-api\n"
        "docker build -t your-dockerhub-username/udagram-api:latest .\n"
        "docker push your-dockerhub-username/udagram-api:latest\n\n"
        "# Build and push frontend\n"
        "cd ../udagram-frontend\n"
        "docker build -t your-dockerhub-username/udagram-frontend:latest .\n"
        "docker push your-dockerhub-username/udagram-frontend:latest"
    )

    pdf.title2("Step 4: Force ECS to Redeploy")
    pdf.code_block(
        "# After pushing new images, force ECS to redeploy:\n"
        "aws ecs update-service --cluster udagram-cluster \\\n"
        "  --service udagram-backend-service --force-new-deployment\n"
        "aws ecs update-service --cluster udagram-cluster \\\n"
        "  --service udagram-frontend-service --force-new-deployment"
    )

    pdf.title2("Step 5: Verify the Deployment")
    pdf.code_block(
        "# Check backend health\n"
        "curl http://app-lb-XXXXXXXXXX.us-east-1.elb.amazonaws.com/health\n\n"
        "# Check API info\n"
        "curl http://app-lb-XXXXXXXXXX.us-east-1.elb.amazonaws.com/\n\n"
        "# Open the ALB URL in your browser\n"
        "# http://app-lb-XXXXXXXXXX.us-east-1.elb.amazonaws.com\n"
        "# Login: test@test.com / password123"
    )

    # ==================== SECTION 11: COST ANALYSIS ====================
    pdf.add_page()
    pdf.title1("11. COST ANALYSIS & NECESSITY OF EACH RESOURCE")

    pdf.paragraph(
        "This section analyzes the cost of running this project on AWS and whether each "
        "resource is truly necessary."
    )

    pdf.title2("Monthly Cost Estimate")
    pdf.table(
        ["Resource", "Estimated Monthly Cost", "Can You Reduce It?"],
        [
            ["RDS db.t4g.micro", "~$15/month", "Use a free t2.micro for 12 months (new accounts)"],
            ["NAT Gateways (x2)", "~$35/month each = $70/month", "YES - this is the biggest cost! Use only 1 NAT or use a public IP for ECS (less secure but free)"],
            ["Elastic IPs (x2)", "~$3.60/month each = $7/month (if unused)", "Free while attached to running NAT gateways"],
            ["ALB", "~$23/month", "Could use Nginx on a single EC2 instance (cheaper but more work)"],
            ["ECS Fargate (4 tasks)", "~$30/month", "Reduce to 1 task each instead of 2"],
            ["CloudWatch Logs", "~$5/month (depends on log volume)", "Reduce retention to 7 days"],
            ["TOTAL", "~$150/month", ""],
        ],
        [45, 55, 80],
    )

    pdf.title2("Which Resources Are Truly Necessary?")

    pdf.title3("Strictly Necessary (Minimum Viable)")
    pdf.bullet("AWS VPC - YES, every AWS application needs a network")
    pdf.bullet("RDS PostgreSQL - YES, the app needs a database")
    pdf.bullet("ECS Fargate (backend) - YES, the API needs to run somewhere")
    pdf.bullet("ALB - YES, needed to route traffic and distribute load")
    pdf.bullet("ECS Task Role + Execution Role - YES, ECS requires these")
    pdf.bullet("Security Groups - YES, required for network security")

    pdf.title3("Can Be Optimized (for learning / lower cost)")
    pdf.bullet("NAT Gateways (2) -> You can use 1 NAT gateway instead of 2. Or use 'assign_public_ip = true' on the ECS tasks and put them in public subnets (less secure but drops $70/month cost).")
    pdf.bullet("ECS desired_count (2 per service) -> Reduce to 1 each. You lose high availability but save ~50% on Fargate costs.")
    pdf.bullet("ALB -> For a learning project, you could expose the backend directly via a public IP on ECS (not recommended for production but fine for testing).")
    pdf.bullet("CloudWatch Logs -> Set retention to 7 days instead of 30 to reduce storage costs.")

    pdf.title3("What's Not Needed for a Minimal Version")
    pdf.bullet("You don't need 2 NAT gateways (one will work)")
    pdf.bullet("You don't need 2 ECS tasks per service (one is enough for learning)")
    pdf.bullet("You don't need 3 pairs of subnets (you could use 1 public and 1 private)")

    pdf.title2("Cost-Saving Tip for Beginners")
    pdf.paragraph(
        "The biggest cost is the 2 NAT Gateways (~$70/month). To eliminate this cost: "
        "change the backend and frontend subnets to public subnets and set "
        "assign_public_ip = true in the ECS services. This is less secure but costs ~$70/month less. "
        "Alternatively, use 1 NAT Gateway in one AZ and route all private subnets through it. "
        "REMEMBER to run 'terraform destroy' when you're done learning!"
    )

    # ==================== SECTION 12: COMMON ISSUES ====================
    pdf.add_page()
    pdf.title1("12. COMMON ISSUES & TROUBLESHOOTING")

    pdf.table(
        ["Problem", "Solution"],
        [
            ["Images not showing in the feed", "The seed data uses picsum.photos URLs. Check if that site is accessible from your network. Also ensure the frontend can reach the API - check that apiUrl in environment.ts has been updated from localhost:8080 to /api/v0"],
            ["Backend ECS tasks keep restarting", "Check CloudWatch logs. Most common cause: the backend can't connect to RDS. Verify the security group allows port 5432 traffic from the backend, and the POSTGRES_HOST env var is correct."],
            ["frontend shows blank page", "Check the browser's JavaScript console for errors. Common cause: the Angular app is trying to call the API with the wrong URL."],
            ["Can't log in", "Make sure you're using test@test.com / password123. If the DB was recreated, the seed would have run again."],
            ["Terraform apply fails", "Check the error message. Common issues: resource limits exceeded (e.g., only 1 NAT per AZ allowed), VPC limit reached, insufficient IAM permissions."],
            ["ALB health check failing", "Check that the backend is listening on port 8080 and the /health endpoint returns 200. Check the backend security group allows traffic from the ALB."],
            ["docker-compose up fails", "Make sure Docker is running. Check if port 5432, 8080, or 80 is already in use."],
            ["How do I see ECS logs?", "aws logs tail /ecs/udagram-backend --follow OR check the CloudWatch console."],
            ["How do I reset everything?", "terraform destroy -auto-approve (destroys all AWS resources). Then run terraform apply again to recreate."],
        ],
        [50, 130],
    )

    # ==================== SECTION 13: HOW TO EXTEND ====================
    pdf.add_page()
    pdf.title1("13. HOW TO EXTEND THE PROJECT")

    pdf.paragraph(
        "Here are practical ways to extend Udagram as a learning exercise, ordered by difficulty:"
    )

    pdf.title2("Beginner Level")
    pdf.bullet("Add more seed data with different images")
    pdf.bullet("Style the feed page with custom CSS")
    pdf.bullet("Add a user profile page showing only their posts")
    pdf.bullet("Add a delete button for feed posts (DELETE endpoint + frontend button)")

    pdf.title2("Intermediate Level")
    pdf.bullet("Add actual image upload: integrate S3 for storing images, add multer middleware to handle file upload, create a presigned URL endpoint")
    pdf.bullet("Add pagination to the feed (page/limit query params)")
    pdf.bullet("Add a 'like' feature (new table, new endpoint, heart button on frontend)")
    pdf.bullet("Add comments on posts (new Comment model, nested routes)")
    pdf.bullet("Add HTTPS: request an ACM certificate, add HTTPS listener on ALB, redirect HTTP to HTTPS")

    pdf.title2("Advanced Level")
    pdf.bullet("Add CI/CD pipeline with GitHub Actions (automatically build Docker images on git push)")
    pdf.bullet("Add Redis caching for the feed endpoint")
    pdf.bullet("Add end-to-end tests with Playwright or Cypress")
    pdf.bullet("Implement refresh token rotation for better JWT security")
    pdf.bullet("Add CloudFront CDN in front of the ALB for global caching")
    pdf.bullet("Set up Blue/Green deployment with ECS and CodeDeploy")

    pdf.title2("Infrastructure Improvements")
    pdf.bullet("Store Terraform state in S3 instead of locally (terraform backend config)")
    pdf.bullet("Add Terraform modules to organize the configuration better")
    pdf.bullet("Add Route53 for a custom domain name")
    pdf.bullet("Add WAF (Web Application Firewall) in front of the ALB")
    pdf.bullet("Set up CloudWatch alarms and SNS notifications for task failures")

    # ==================== FINAL NOTES ====================
    pdf.ln(10)
    pdf.set_draw_color(25, 60, 120)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)
    pdf.set_font("DejaVu", "I", 10)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(0, 5.5,
        "This guide was automatically generated from the Udagram project source code. "
        "The project is designed as a learning tool to demonstrate full-stack development "
        "and cloud deployment. Every resource, configuration, and line of code has been "
        "documented to help beginners understand how a real-world web application works "
        "from end to end."
    )

    # Save
    output_path = "/home/big-kola/Desktop/Udagram_Complete_Project_Guide.pdf"
    # Ensure Desktop directory exists
    os.makedirs("/home/big-kola/Desktop", exist_ok=True)
    pdf.output(output_path)
    print(f"PDF saved to {output_path}")
    print(f"Total pages: {pdf.page_no()}")


if __name__ == "__main__":
    build_pdf()
