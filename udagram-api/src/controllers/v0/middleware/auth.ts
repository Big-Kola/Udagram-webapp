import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';
import { config } from '../../../config/config';

export function requireAuth(req: Request, res: Response, next: NextFunction): void {
  const authHeader = req.headers.authorization;
  if (!authHeader) {
    res.status(401).json({
      message: 'authorization header required',
      hint: 'add header: Authorization: Bearer <token>',
    });
    return;
  }
  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, config.jwtSecret);
    (req as any).user = decoded;
    next();
  } catch (err) {
    res.status(401).json({
      message: 'invalid or expired token',
      hint: 'login again via POST /api/v0/users/login to get a fresh token',
      error: err instanceof Error ? err.message : String(err),
    });
  }
}
