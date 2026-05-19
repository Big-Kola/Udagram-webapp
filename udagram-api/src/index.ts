import app, { sequelize } from './server';
import { v0Router } from './controllers/v0';

const PORT = process.env.PORT || 8080;

async function start(): Promise<void> {
  try {
    await sequelize.authenticate();
    console.log('Database connected');
    await sequelize.sync();
    console.log('Models synced');
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
