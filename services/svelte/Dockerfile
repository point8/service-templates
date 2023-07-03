# Build stage
FROM node:18.16.1-bullseye-slim AS build

WORKDIR /usr/src/app
COPY ./ /usr/src/app/

RUN npm ci &&\
    npm run build

# Execution stage
FROM gcr.io/distroless/nodejs:18

# USER node
ENV NODE_ENV production
WORKDIR /usr/src/app

COPY --chown=node:node --from=build /usr/src/app/package*.json /usr/src/app/
COPY --chown=node:node --from=build /usr/src/app/node_modules /usr/src/app/node_modules
COPY --chown=node:node --from=build /usr/src/app/build /usr/src/app/build

CMD ["build"]
