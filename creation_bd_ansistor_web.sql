drop table productos;
drop table user;
drop table user_product;
drop table user_session;
drop table notificaciones;
drop table question;
drop table answer;


create table productos (
    id_producto int not null, CONSTRAINT producto_pk_const PRIMARY KEY(id_producto),
    nombre VARCHAR(50),
    precio int,
    descripcion VARCHAR(200)
);

create table user (
    id_user int not null, CONSTRAINT user_pk_const PRIMARY KEY(id_user),
    nombre VARCHAR(50),
    apellidos VARCHAR(100),
    telefono VARCHAR(10),
    id_producto int not null, CONSTRAINT user_fk_const FOREIGN KEY  (id_producto) REFERENCES productos(id_producto)
);

create table user_product (
    id_producto int not null, CONSTRAINT user_pro_fk1_const FOREIGN KEY  (id_producto) REFERENCES productos(id_producto),
    id_user int not null, CONSTRAINT user_pro_fk2_const FOREIGN KEY  (id_user) REFERENCES user(id_user),
    license_type VARCHAR(50) CHECK (license_type IN ('mensual', 'anual','for life')),
    license_cad int
);

create table user_session (
    id_user int not null, CONSTRAINT user_session_fk_const FOREIGN KEY  (id_user) REFERENCES user(id_user),
    state VARCHAR (20) CHECK (state IN ('login', 'logout')),
    last_login datetime,
    device VARCHAR(30)
);

create table notificaciones (
    id_user int not null, CONSTRAINT notificaciones_fk_const FOREIGN KEY  (id_user) REFERENCES user(id_user),
    mensaje VARCHAR(200),
    title VARCHAR(50),
    state VARCHAR(20) CHECK (state IN ('read', 'nonread'))
);

create table question (
    id_quest int not null, CONSTRAINT quest_pk_const PRIMARY KEY(id_quest),
    id_user int not null, CONSTRAINT quest_fk_const FOREIGN KEY  (id_user) REFERENCES user(id_user),
    question VARCHAR(350),
    type VARCHAR(100) CHECK (type IN ('error', 'duda','sugerencia')),
    id_producto int not null, CONSTRAINT quest_fk2_const FOREIGN KEY  (id_producto) REFERENCES productos(id_producto)
);

create table answer (
    id_answer int not null, CONSTRAINT answ_pk_const PRIMARY KEY(id_answer),
    id_quest int not null, CONSTRAINT answ_fk_const FOREIGN KEY  (id_quest) REFERENCES question(id_quest),
    id_user int not null, CONSTRAINT answ_fk2_const FOREIGN KEY  (id_user) REFERENCES user(id_user),
    answer VARCHAR(400)
);