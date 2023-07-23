FROM php:8.2-fpm-alpine
RUN apk update; \
    apk upgrade;
RUN apk add libzip-dev
RUN docker-php-ext-install pdo pdo_mysql
RUN apk add --no-cache pcre-dev $PHPIZE_DEPS \
        && pecl install redis \
        && docker-php-ext-enable redis.so
