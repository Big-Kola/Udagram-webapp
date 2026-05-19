import { Router, Request, Response } from 'express';
import { User } from './UserModel';
import jwt from 'jsonwebtoken';
import { config } from '../../../config/config';

export const userRouter = Router();

userRouter.post('/register', async (req: Request, res: Response) => {
  const { email, password } = req.body;
  if (!email || !password) {
    return res.status(400).send({ message: 'email and password are required' });
  }
  const existing = await User.findOne({ where: { email } });
  if (existing) {
    return res.status(409).send({ message: 'email already registered' });
  }
  const passwordHash = await User.hashPassword(password);
  const user = await User.create({ email, passwordHash });
  const token = jwt.sign({ id: user.id, email: user.email }, config.jwtSecret, { expiresIn: '7d' });
  res.status(201).send({ token, user: { id: user.id, email: user.email } });
});

userRouter.post('/login', async (req: Request, res: Response) => {
  const { email, password } = req.body;
  if (!email || !password) {
    return res.status(400).send({ message: 'email and password are required' });
  }
  const user = await User.findOne({ where: { email } });
  if (!user) {
    return res.status(401).send({ message: 'invalid credentials' });
  }
  const valid = await user.validatePassword(password);
  if (!valid) {
    return res.status(401).send({ message: 'invalid credentials' });
  }
  const token = jwt.sign({ id: user.id, email: user.email }, config.jwtSecret, { expiresIn: '7d' });
  res.send({ token, user: { id: user.id, email: user.email } });
});
