import { Model, DataTypes } from 'sequelize';
import { sequelize } from '../../../server';
import bcrypt from 'bcrypt';
import { config } from '../../../config/config';

export class User extends Model {
  public id!: number;
  public email!: string;
  public passwordHash!: string;
  public createdAt!: Date;
  public updatedAt!: Date;

  public static async hashPassword(password: string): Promise<string> {
    return bcrypt.hash(password, config.bcryptSaltRounds);
  }

  public async validatePassword(password: string): Promise<boolean> {
    return bcrypt.compare(password, this.passwordHash);
  }
}

User.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    email: {
      type: DataTypes.STRING(128),
      allowNull: false,
      unique: true,
    },
    passwordHash: {
      type: DataTypes.STRING(256),
      allowNull: false,
    },
  },
  {
    tableName: 'users',
    sequelize,
  }
);
