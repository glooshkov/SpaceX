# build environment
FROM node:10.5.2-alpine as build
WORKDIR /frontend
ENV PATH /frontend/node_modules/.bin:$PATH
COPY package.json /frontend/package.json
RUN npm install --silent
COPY . /frontend
RUN npm run build
#EXPOSE 5173

# production environment
FROM nginx:1.16.0-alpine
COPY --from=build /frontend/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
EXPOSE 80
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]