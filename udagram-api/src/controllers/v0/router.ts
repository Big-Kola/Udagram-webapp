import { Router } from 'express';
import { feedRouter } from './feed/FeedController';
import { userRouter } from './users/UserController';

export { requireAuth } from './middleware/auth';

export const v0Router = Router();

v0Router.use('/feed', feedRouter);
v0Router.use('/users', userRouter);
