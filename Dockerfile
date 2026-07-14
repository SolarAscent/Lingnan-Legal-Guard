FROM node:20-bookworm-slim AS frontend-builder

WORKDIR /app/vue-legal-guard
COPY vue-legal-guard/package*.json ./
RUN npm ci
COPY vue-legal-guard/ ./
RUN npm run build

FROM node:20-bookworm-slim

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    libreoffice \
    fonts-noto-cjk \
    fontconfig \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app/server
COPY server/package*.json ./
RUN npm ci --omit=dev
COPY server/ ./
COPY --from=frontend-builder /app/vue-legal-guard/dist ./public

ENV NODE_ENV=production
ENV PORT=3001
EXPOSE 3001

CMD ["npm", "run", "start"]
