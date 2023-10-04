create table Customer (
    customer_ID int not null,
    email varchar(255) not null,
    address varchar(255) not null,
    personal_no double not null,
    customer_password varchar(255) not null,
    customer_name varchar(255) not null,
    phone_no double not null,
    newsletter boolean not null,
    unique(
        customer_ID,
        email,
        personal_no
    ),
    primary key(customer_ID)
);
