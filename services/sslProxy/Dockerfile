# Can be located at https://archive.org/details/nginx_1.9.8.tar if needed
FROM nginx:1.26.0@sha256:192e88a0053c178683ca139b9d9a2afb0ad986d171fae491949fe10970dd9da9 as base

COPY nginx.conf /etc/nginx/nginx.conf
COPY mcouniverse.pem /etc/nginx/mcouniverse.pem
COPY private_key.pem /etc/nginx/private_key.pem
COPY fullchain1.pem /etc/nginx/fullchain1.pem
COPY privkey1.pem /etc/nginx/privkey1.pem
