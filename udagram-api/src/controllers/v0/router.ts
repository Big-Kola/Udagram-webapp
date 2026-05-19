import { Router, Request, Response, NextFunction } from 'express';
import { feedRouter } from './feed/FeedController';
import { userRouter } from './users/UserController';
import jwt from 'jsonwebtoken';
import { config } from '../../config/config';

export function requireAuth(req: Request, res: Response, next: NextFunction): void {
  const authHeader = req.headers.authorization;
  if (!authHeader) {
    res.status(401).send({ message: 'authorization header required' });
    return;
  }
  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, config.jwtSecret);
    (req as any).user = decoded;
    next();
  } catch {
    res.status(401).send({ message: 'invalid or expired token' });
  }
}

export const v0Router = Router();

v0Router.use('/feed', feedRouter);
v0Router.use('/users', userRouter);
