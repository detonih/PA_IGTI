FROM node:13-alpine

WORKDIR /web
# Adicionando `/web/node_modules/.bin` para o $PATH
ENV PATH /web/node_modules/.bin:$PATH
# Instalando dependências da aplicação e armazenando em cache.
COPY package.json /web/package.json
RUN npm install --silent
RUN npm install react-scripts@3.3.1 -g --silent
RUN npm install axios --silent
# Inicializa a aplicação
CMD ["npm", "start"]