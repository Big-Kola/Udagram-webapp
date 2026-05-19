import { Router, Request, Response } from 'express';
import { FeedItem } from './FeedModel';
import { requireAuth } from '../router';

export const feedRouter = Router();

feedRouter.get('/', async (req: Request, res: Response) => {
  const items = await FeedItem.findAndCountAll({ order: [['id', 'DESC']] });
  res.send(items);
});

feedRouter.post('/', requireAuth, async (req: Request, res: Response) => {
  const { caption, url } = req.body;
  if (!caption || !url) {
    return res.status(400).send({ message: 'caption and url are required' });
  }
  const item = await FeedItem.create({ caption, url });
  res.status(201).send(item);
});

feedRouter.get('/:id', async (req: Request, res: Response) => {
  const item = await FeedItem.findByPk(req.params.id);
  if (!item) {
    return res.status(404).send({ message: 'Feed item not found' });
  }
  res.send(item);
});
