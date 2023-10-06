FROM arm64v8/nginx:1.25.2-alpine AS prod

COPY nginx.conf /etc/nginx/nginx.conf
COPY proxy_params /etc/nginx/proxy_params
COPY timskiproekt.conf /etc/nginx/sites-available/timskiproekt.conf

RUN mkdir /etc/nginx/sites-enabled

RUN ln -s /etc/nginx/sites-available/timskiproekt.conf /etc/nginx/sites-enabled/timskiproekt.conf

CMD ["nginx", "-g", "daemon off;"]

FROM arm64v8/nginx:1.25.2-alpine AS dev

COPY nginx.conf /etc/nginx/nginx.conf
COPY proxy_params /etc/nginx/proxy_params
COPY local.conf /etc/nginx/sites-available/local.conf

RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/local.conf /etc/nginx/sites-enabled/local.conf

CMD ["nginx", "-g", "daemon off;"]