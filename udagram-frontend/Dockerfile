FROM node:18-alpine AS builder

WORKDIR /app

RUN npm install -g @ionic/cli

COPY package*.json ./
RUN npm install

COPY . .

RUN ionic build


FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

# FIXED LINE 👇
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]