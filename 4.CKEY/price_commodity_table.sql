CREATE TABLE price (
   id INT NOT NULL, 
   price_date DATE NOT NULL,
   open DECIMAL(10, 6 ) NULL,
   high DECIMAL(10, 6 ) NULL,
   low DECIMAL(10, 6 ) NULL,
   close DECIMAL(10, 6 ) NULL,
   volume DECIMAL(10, 6 ) NULL,
   adjusted DECIMAL(10, 6 ) NULL,
   PRIMARY KEY (id, price_date)
);I
