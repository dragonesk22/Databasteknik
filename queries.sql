# Query to grab welcome text from homepage
SELECT descr
from Department
where dep_ID="1000";

#Query to get top level departments with relevant information for the homepage : title, short desc, link
select * from Parent_Relation;
SELECT
    title, descr, link
FROM
    Department
WHERE
    dep_ID IN (SELECT 
            child_ID
        FROM
            Parent_Relation
        WHERE
            parent_ID = '1000');

#Query to get featured products from homepage, including their title, desc, price, and a link to their page
SELECT 
    title, prod_desc, prod_price, prod_link
FROM
    Product
WHERE
    prod_ID IN (SELECT 
            prod_ID
        FROM
            Featured);
            
#Query to get all products that are keyword-related to a chosen product - in this case the "Banana"
SELECT DISTINCT
    P2.title
FROM
    Product AS P1
        JOIN
    Product_Keywords AS PK1 ON P1.prod_ID = PK1.prod_ID
        JOIN
    Product_Keywords AS PK2 ON PK1.keyword = PK2.keyword
        JOIN
    Product AS P2 ON PK2.prod_ID = P2.prod_ID
WHERE
    P1.title = 'banana'
        AND P2.title != 'banana';
        

        
#Query to list all products within a certain department (in this case, Computers) along with their title, desc, price, avg rating
SELECT
	P1.title, P1.prod_desc, P1.prod_price - (P1.prod_price * P1.percent_discount) + (prod_price * VAT), P1.avg_rating
FROM
	Product as P1
    join
    Department as D1 on P1.dep_ID = D1.dep_ID 
WHERE
	D1.link='Computers';

#Query to list all sale products by discount percentage largest to smallest
select prod_ID, title, percent_discount, (prod_price - (prod_price * percent_discount) + (prod_price * VAT))
from Product
order by percent_discount desc;


####

