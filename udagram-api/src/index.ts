import app, { sequelize } from './server';
import { v0Router } from './controllers/v0';
import { FeedItem } from './controllers/v0/feed/FeedModel';
import { User } from './controllers/v0/users/UserModel';

const PORT = process.env.PORT || 8080;

async function seed(): Promise<void> {
  const userCount = await User.count();
  if (userCount === 0) {
    const user = await User.create({
      email: 'test@test.com',
      passwordHash: await User.hashPassword('password123'),
    });
    console.log('Seeded test user: test@test.com / password123');

    await FeedItem.bulkCreate([
      { caption: 'Welcome to Udagram!', url: 'https://picsum.photos/400/300?random=1' },
      { caption: 'Learning AWS deployment', url: 'https://picsum.photos/400/300?random=2' },
      { caption: 'My first post', url: 'https://picsum.photos/400/300?random=3' },
    ]);
    console.log('Seeded 3 sample feed items');
  }
}

async function start(): Promise<void> {
  try {
    await sequelize.authenticate();
    console.log('Database connected');

    const isProduction = process.env.NODE_ENV === 'production';
    await sequelize.sync({ force: !isProduction });
    console.log(`Tables synced (force=${!isProduction})`);

    await seed();
  } catch (err) {
    console.error('Database connection failed:', err);
    process.exit(1);
  }

  app.use('/api/v0', v0Router);

  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
}

start();
