variable "aws_region" {
  type        = string
  description = "AWS_region"
}

variable "db_password" {
  type        = string
  description = "PostgreSQL master password"
  sensitive   = true
}

variable "jwt_secret" {
  type        = string
  description = "JWT signing secret"
  sensitive   = true
}

variable "backend_image" {
  type        = string
  description = "Docker image URL for the backend API"
}

variable "frontend_image" {
  type        = string
  description = "Docker image URL for the frontend"
}
