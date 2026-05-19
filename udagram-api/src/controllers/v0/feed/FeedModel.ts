import { Model, DataTypes } from 'sequelize';
import { sequelize } from '../../../server';

export class FeedItem extends Model {
  public id!: number;
  public caption!: string;
  public url!: string;
  public createdAt!: Date;
  public updatedAt!: Date;
}

FeedItem.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    caption: {
      type: DataTypes.STRING(256),
      allowNull: false,
    },
    url: {
      type: DataTypes.STRING(512),
      allowNull: false,
    },
  },
  {
    tableName: 'feed',
    sequelize,
  }
);
