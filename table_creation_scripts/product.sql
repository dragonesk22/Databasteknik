create table Product (
    prod_ID int not null,
    title varchar(255) not null,
    prod_link varchar(255),
    available boolean not null,
    prod_desc varchar(255),
    avg_rating int,
    dep_ID int not null,
    stock int not null,
    primary key (
        prod_ID
    ),
    unique (
        title,
        prod_link
    ),
    foreign key(dep_ID) references Department(dep_ID)
    );
