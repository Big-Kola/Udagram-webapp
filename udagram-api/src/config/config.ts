export const config = {
  host: process.env.POSTGRES_HOST || 'localhost',
  port: parseInt(process.env.POSTGRES_PORT || '5432'),
  database: process.env.POSTGRES_DB || 'udagram',
  username: process.env.POSTGRES_USERNAME || 'postgres',
  password: process.env.POSTGRES_PASSWORD || 'password',
  dialect: 'postgres' as const,
  jwtSecret: process.env.JWT_SECRET || 'udagram-jwt-secret',
  bcryptSaltRounds: 10,
};
