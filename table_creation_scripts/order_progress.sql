CREATE TABLE Order_Progress (
    payment_ref INT NOT NULL,
    order_status VARCHAR(255) NOT NULL,
    last_changed TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP,
    date_created TIMESTAMP DEFAULT current_timestamp,
    date_opened TIMESTAMP,
    date_dispatched TIMESTAMP,
    
    primary key (payment_ref)
);

