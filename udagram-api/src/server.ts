import express, { Request, Response, NextFunction } from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import { Sequelize } from 'sequelize';
import { config } from './config/config';

export const sequelize = new Sequelize(config.database, config.username, config.password, {
  host: config.host,
  port: config.port,
  dialect: config.dialect,
  logging: console.log,
});

const app = express();

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.json({
    name: 'Udagram API',
    version: '1.0.0',
    endpoints: {
      health: 'GET /health',
      register: 'POST /api/v0/users/register',
      login: 'POST /api/v0/users/login',
      feed: 'GET /api/v0/feed',
      createFeed: 'POST /api/v0/feed',
      feedItem: 'GET /api/v0/feed/:id',
    },
  });
});

app.get('/health', (req, res) => {
  res.send({ status: 'ok' });
});

app.use((err: Error, req: Request, res: Response, _next: NextFunction) => {
  console.error('Unhandled error:', err);
  res.status(500).json({ message: err.message, stack: err.stack });
});

export default app;
